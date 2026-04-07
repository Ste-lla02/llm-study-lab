import os
import logging
from pathlib import Path

import telebot
from dotenv import load_dotenv
from openai import OpenAI

# Config
load_dotenv(override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CSV_PATH = os.getenv("CSV_PATH", "animals.csv")
MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY non trovata.")

if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN non trovata.")

if not Path(CSV_PATH).exists():
    raise FileNotFoundError(f"CSV non trovato: {CSV_PATH}")

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)


# Client
client = OpenAI(api_key=OPENAI_API_KEY)
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN, parse_mode=None)

CSV_FILE_ID = None

# File Upload
def upload_csv_once() -> str:
    global CSV_FILE_ID

    if CSV_FILE_ID is not None:
        return CSV_FILE_ID

    logger.info("Caricamento CSV...")
    with open(CSV_PATH, "rb") as f:
        uploaded_file = client.files.create(
            file=f,
            purpose="user_data"
        )

    CSV_FILE_ID = uploaded_file.id
    logger.info("CSV caricato con file_id=%s", CSV_FILE_ID)
    return CSV_FILE_ID


def parse_mode_and_prompt(user_text: str) -> tuple[str, str]:
    """
    Esempi supportati:
    - analisi: quali animali vivono nella savana?
    - storytelling: raccontami una storia su Leo
    - quiz: fammi una domanda sugli animali pericolosi
    """
    if not user_text:
        return "analisi", ""

    text = user_text.strip()

    lowered = text.lower()
    if lowered.startswith("analisi:"):
        return "analisi", text[len("analisi:"):].strip()

    if lowered.startswith("storytelling:"):
        return "storytelling", text[len("storytelling:"):].strip()

    if lowered.startswith("quiz:"):
        return "quiz", text[len("quiz:"):].strip()

    # default
    return "analisi", text


# Prompt builder
def build_system_prompt(mode: str) -> str:
    if mode == "analisi":
        return (
            "Sei un assistente che analizza un file CSV sugli animali. "
            "Rispondi in modo chiaro, sintetico e accurato. "
            "Usa solo le informazioni presenti nel file. "
            "Se qualcosa non è presente nel CSV, dichiaralo esplicitamente. "
            "Non inventare animali, colonne, valori o relazioni."
        )

    if mode == "storytelling":
        return (
            "Sei un narratore creativo che usa un file CSV sugli animali come base dei personaggi. "
            "Puoi scrivere una breve storia, ma devi rispettare i dati presenti nel CSV. "
            "Usa solo animali presenti nel file. "
            "Mantieni coerenza con habitat, personalità, livello di pericolo e descrizione. "
            "Non inventare fatti che contraddicono il dataset."
        )

    if mode == "quiz":
        return (
            "Sei un creatore di quiz basati su un file CSV sugli animali. "
            "Genera una sola domanda alla volta. "
            "La domanda deve essere basata solo sui dati presenti nel file. "
            "Fornisci sempre:\n"
            "1. domanda\n"
            "2. tre opzioni (A, B, C)\n"
            "3. risposta corretta\n"
            "4. breve spiegazione\n"
            "Non inventare informazioni non presenti nel CSV."
        )

    return (
        "Sei un assistente utile che analizza un CSV. "
        "Usa solo i dati presenti nel file."
    )


def build_user_prompt(mode: str, user_prompt: str) -> str:
    if mode == "analisi":
        return (
            f"Domanda dell'utente: {user_prompt}\n\n"
            "Se utile, organizza la risposta in punti brevi. "
            "Se la richiesta è ambigua, prova a interpretarla in modo ragionevole senza inventare dati."
        )

    if mode == "storytelling":
        return (
            f"Richiesta narrativa dell'utente: {user_prompt}\n\n"
            "Scrivi una storia breve, massimo 200 parole. "
            "Il tono deve essere giocoso, leggibile e coerente con i dati del CSV. "
            "Se l'utente cita un animale non presente nel file, dillo chiaramente."
        )

    if mode == "quiz":
        return (
            f"Richiesta quiz dell'utente: {user_prompt}\n\n"
            "Crea un quiz in italiano. "
            "Formato obbligatorio:\n"
            "Domanda: ...\n"
            "A) ...\n"
            "B) ...\n"
            "C) ...\n"
            "Risposta corretta: ...\n"
            "Spiegazione: ...\n"
        )

    return user_prompt


# Chiamata LLM
def ask_llm(user_text: str) -> str:
    mode, clean_prompt = parse_mode_and_prompt(user_text)

    if not clean_prompt:
        return (
            "Scrivi una richiesta, per esempio:\n"
            "- analisi: quali animali vivono nella savana?\n"
            "- storytelling: raccontami una storia su Leo e Kiki\n"
            "- quiz: fammi una domanda sugli animali pericolosi"
        )

    file_id = upload_csv_once()
    system_prompt = build_system_prompt(mode)
    user_prompt = build_user_prompt(mode, clean_prompt)

    response = client.responses.create(
        model=MODEL_NAME,
        input=[
            {
                "role": "system",
                "content": [
                    {"type": "input_text", "text": system_prompt}
                ]
            },
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": user_prompt},
                    {"type": "input_file", "file_id": file_id}
                ]
            }
        ]
    )

    return response.output_text.strip()



# Telegram handlers
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    text = (
        "Ciao! 🐾\n"
        "Sono un bot sugli animali basato su un CSV.\n\n"
        "Modalità disponibili:\n"
        "- analisi\n"
        "- storytelling\n"
        "- quiz\n\n"
        "Esempi:\n"
        "analisi: quali animali vivono nella savana?\n"
        "storytelling: raccontami una storia su Leo e Zara\n"
        "quiz: fammi una domanda sugli animali acquatici"
    )
    bot.reply_to(message, text)


@bot.message_handler(func=lambda message: True, content_types=["text"])
def handle_text(message):
    user_prompt = message.text.strip()

    try:
        logger.info("Messaggio da user_id=%s", message.from_user.id)
        bot.send_chat_action(message.chat.id, "typing")

        answer = ask_llm(user_prompt)
        bot.reply_to(message, answer)

    except Exception:
        logger.exception("Errore nella gestione del messaggio")
        bot.reply_to(
            message,
            "Si è verificato un errore durante l'elaborazione della richiesta."
        )


if __name__ == "__main__":
    upload_csv_once()
    logger.info("Bot avviato.")
    bot.infinity_polling(skip_pending=True, timeout=30)