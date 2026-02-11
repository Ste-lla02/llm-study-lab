# 🪟 The context window

When working with Large Language Models (LLMs), there is a fundamental constraint we must always keep in mind:
the **context window**.

> The context window is the maximum number of tokens a model can consider at once when generating the next token.


In other words, it is the maximum length of the input sequence the model can look back on. If we exceed this limit, the model simply cannot process the request.

---

## 🧠 What actually fits inside the context window?
A very common misunderstanding is to think that the context window only applies to your latest message. That is not the case.  

What must fit inside the context window is:
- the system prompt;
- all previous user messages;
- all previous assistant replies;
- the current user message;
- all tokens generated so far during the response.

LLMs generate output one token at a time. After each generated token, the entire sequence (input + generated tokens so far) is fed back into the model to predict the next token.


So the context window must contain:
> the full conversation history plus the partial answer being generated.


---
