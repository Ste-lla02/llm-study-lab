# 🐾 Animal LLM Telegram Bot

## 🎯 Objective

This project demonstrates how to build a **simple LLM-based application** using:

* a **CSV dataset**
* the **OpenAI API**
* a **Telegram bot interface**

The goal is to show how the **same data source** can support **multiple interaction modes** by leveraging prompt engineering.

Instead of treating the model as a static tool, we design it as a **dynamic system** that adapts its behavior based on user intent.

---

## 📊 Dataset Design

The dataset is intentionally designed to be:

* **structured** → for factual queries
* **semantic** → for reasoning and storytelling
* **lightweight** → suitable for direct LLM ingestion

### Example structure:

```csv
name,species,age,habitat,personality,danger_level,favorite_food,description
Leo,lion,8,savannah,dominant,high,meat,"A proud lion who loves watching over the savannah."
Milo,cat,2,home,playful,low,fish,"A curious house cat who enjoys chasing shadows."
Zara,zebra,5,savannah,shy,medium,grass,"A gentle zebra that prefers staying close to the herd."
```

LLMs work better when data is not only numerical but also **rich in meaning**.
Adding fields like:

* `personality`
* `description`
* `habitat`

enables more advanced behaviors such as reasoning and storytelling.

---

## ⚙️ System Architecture

The system consists of three main components:

1. **Telegram Bot**
2. **LLM (OpenAI API)**
3. **CSV Dataset**

### Flow:

1. The user sends a message via Telegram
2. The bot parses the message to detect the interaction mode
3. A specific prompt is generated
4. The CSV is attached to the request
5. The LLM produces a response
6. The bot sends the response back to the user

---

## 🧠 Python Workflow

The Python script is structured into logical steps:

### 1. Configuration

* Load environment variables (`.env`)
* Initialize API clients (OpenAI + Telegram)

### 2. File Handling

* Upload the CSV file **once**
* Store and reuse the `file_id`

👉 This avoids repeated uploads and improves efficiency

### 3. Mode Parsing

The bot detects how the user wants to interact:

```text
analisi: ...
storytelling: ...
quiz: ...
```

Default mode: `analysis`

### 4. Prompt Engineering

Different **system prompts** are used depending on the mode:

* analytical assistant
* creative storyteller
* quiz generator

This is the core idea of the project:
👉 **same model + same data → different behaviors**


### 5. LLM Request

The request includes:

* system prompt (role definition)
* user prompt (task)
* CSV file (data source)

### 6. Response Handling

* Extract model output
* Send it back to Telegram
* Handle errors gracefully

---

## 🤖 Interaction Modes

The bot supports **three distinct modes**:

### 📊 1. Analysis Mode

**Purpose:**
Answer factual questions using the dataset.

**Example:**

```text
analisi: which animals live in the savannah?
```

### 📖 2. Storytelling Mode

**Purpose:**
Generate short stories using dataset entities.

**Example:**

```text
storytelling: tell me a story about Leo and Kiki
```

### 🎯 3. Quiz Mode

**Purpose:**
Generate quiz questions based on the dataset.

**Example:**

```text
quiz: ask me a question about dangerous animals
```

**Output format:**

```
Question: ...
A) ...
B) ...
C) ...
Correct answer: ...
Explanation: ...
```

---

## 💡 Key Insight

This project highlights a fundamental concept in LLM applications:

> **The behavior of a model is not fixed — it is shaped by the prompt.**

With:

* the same dataset
* the same model

we can obtain:

* analytical reasoning
* creative storytelling
* structured quiz generation

This is achieved through **prompt specialization and role conditioning**.

---

## 📦 Requirements

```bash
pip install openai pyTelegramBotAPI python-dotenv
```

---

## 🔐 Environment Variables

```env
OPENAI_API_KEY=your_api_key
TELEGRAM_BOT_TOKEN=your_bot_token
CSV_PATH=data/animals.csv
OPENAI_MODEL=gpt-4.1-mini
```

---


## 🐾 Final Note

Even though this is a simple project, it captures a powerful idea:

👉 **LLMs are not just models — they are programmable interfaces over data.**
