# Fun fact ✨ – Running Ollama as a local server 🧠🖥️

Ollama can be used as a **local inference server** that runs in the background and can be accessed programmatically.

---

## Ollama runs as a local service 🚀

After installing Ollama from:

> https://ollama.com

the Ollama server usually **starts automatically** in the background. To verify that Ollama is running locally, open a browser and visit:
> http://localhost:11434

If everything is working correctly, you should see: `Ollama is running`.

This confirms that:
- the Ollama server is active,
- models can be served locally,
- inference is happening entirely on your machine.

---

## Starting the server manually (if needed) ⚙️

If the server is not running, you can start it manually.

Open a terminal (macOS/Linux) or PowerShell (Windows) and run:

```bash
ollama serve
```
Then, in another terminal, pull a model: `ollama pull llama3.2`
Now refresh:
> http://localhost:11434

and verify that the service is reachable.

---
## Choosing lighter models for slower machines 🐢
Running LLMs locally is constrained by: available RAM, CPU/GPU capabilities,
and model size.
So, if Ollama feels slow on your machine, you can switch to a smaller variant.

---

## Which models can run locally with Ollama? 📦  

Ollama supports a growing ecosystem of open-weight models, 
including: LLaMA family, DeepSeek models, and other popular options (Mistral, Phi models, Qwen, Gemma, and more)

It is possible to search all the available models at:
> https://ollama.com/search?page=2

---

## Managing local models with Ollama 🗂️

When working with Ollama, it is important to distinguish between:
- **available models** (supported by Ollama),
- **installed models** (already downloaded on your machine).

Ollama keeps models **locally on disk**, and once a model is downloaded it can be reused
without downloading it again.

---

### Listing locally installed models

To check which models are already available **locally** on your machine, run:

```bash
ollama list
```

---

## Summary
`ollama pull` → installs a model locally  
`ollama list` → inspects the local model registry  
`ollama run model_name` → perform inference using installed models



