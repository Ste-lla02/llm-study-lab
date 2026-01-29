# Fun fact ✨ – Running LLMs locally with Ollama 🦙

One important tool in the ecosystem of generative AI is **Ollama**.

Ollama (https://ollama.com) is a platform that allows you to **run large language models locally** on your own machine, without relying on cloud-based APIs. This makes it particularly useful for experimentation, privacy-sensitive tasks, and learning how LLMs behave in a controlled environment.

---

## Why Ollama is interesting 👓

- Models run **entirely on your local hardware**
- No internet connection is required after installation
- No API keys or external services are needed
- It supports several open-weight models (e.g. LLaMA-family models, Phi, Mistral, etc.)

This makes Ollama a practical tool for studying generative models from a hands-on perspective.

---

## Running a model locally 👩🏻‍💻

Once Ollama is installed, you can start a model directly from the terminal.

For example, to run the **Phi-3** model:

```bash
ollama run phi3
```

This command:  
1. Downloads the model (if it is not already available locally)
2. Starts an interactive chat session with the model
3. Allows you to use the model as a conversational agent directly from the terminal

---

## Interacting with the model 💬
After running the command, you can type prompts directly into the terminal and receive responses from the model, similar to a chat interface.
To exit the chat session, simply press:  
- ```Ctrl + D``` (Linux / Windows)  
- ```Cmd + D``` (macOS)  
This will close the interaction and return control to the terminal.