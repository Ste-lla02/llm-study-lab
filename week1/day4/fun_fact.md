# Fun fact ✨ – Models
The current landscape of Large Language Models (LLMs) includes both **proprietary** and **open-source** solutions, developed by different organizations and optimized for different use cases.  

---


### Proprietary models 🔒
- GPT — developed by [OpenAI](https://www.openai.com)
- Claude — developed by [Anthropic](https://www.anthropic.com)
- Gemini — developed by Google
- Grok — developed by [xAI](https://x.ai)
- Mistral (commercial models) — developed by [Mistral AI](https://mistral.ai/it) 

These models are typically accessed through cloud-based services, often via paid APIs or hosted applications.

### Open-source and open-weight models 🔓
- LLaMA — developed by [Meta](https://www.meta.ai)
- Mixtral — developed by [Mistral AI](https://mistral.ai)
- Gemma — developed by Google
- GPT-OSS — released by OpenAI
- Phi — developed by [Microsoft](https://www.microsoft.com)
- DeepSeek — developed by [DeepSeek AI](https://www.deepseek.com/en/)
- Qwen — developed by [Alibaba Cloud](https://www.alibabacloud.com/en?_p_lc=7&utm_content=se_1021723812&gclid=CjwKCAiAs4HMBhBJEiwACrfNZRZGD1sSgQEwFZSvpX1ZiyUnBCRL6PA_LT2n3AtkkpwG8d7qKkvxDxoCbd0QAvD_BwE)

These models can often be downloaded, fine-tuned, and executed locally, depending on hardware constraints and licensing terms.

---

## Model vs Product: an important distinction
It is crucial to distinguish between using a model and using a product built on top of a model.  
A **model** is a trained neural network with fixed parameters that performs inference.  
A **product** is an interface or service that exposes the model to users.  
For example:
- When we use ChatGPT, we are not directly using the GPT model itself, but a chat-based product built on top of a GPT model.
- The same underlying model can be exposed through different products.

### Common ways to access models 🛠️
1. Chat interfaces: User-friendly conversational products (e.g., ChatGPT, Claude Chat).
2. Cloud APIs: Programmatic access to hosted models via HTTP requests.
3. Direct inference: Local or self-hosted execution of models, where inference happens on the user’s machine
(e.g., running a model locally via Ollama).


This distinction helps clarify that the model, the interface, and the deployment strategy are separate layers, each with different implications in terms of cost, latency, privacy, and control.