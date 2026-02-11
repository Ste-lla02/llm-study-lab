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

## 🎭 Context window and the illusion of memory
This connects directly to the illusion of memory. LLMs do not remember anything across API calls. Indeed, they only appear to remember because we keep resending the conversation history.

The context window defines: how much “past” the model can see, how much information it can use to stay coherent, 
how many references it can keep track of.


When the context window **fills up**, something has to be dropped:
- earlier messages are truncated
- summaries replace raw history
- or the request fails entirely  

This is why long conversations eventually “forget” earlier details.

---

## 🧩 Why context window size is so important

A larger context window enables: long and coherent conversations, multi-shot prompting (many examples in the prompt), Retrieval-Augmented Generation (RAG) with large documents, 
and reasoning over long texts (papers, logs, codebases).


In particular, many inference-time techniques rely heavily on having enough context to work with.
Without sufficient context:
- examples cannot fit;
- references are lost;
- reasoning quality degrades.

---

## 📏 How big are context windows, roughly?

Different models support very different context window sizes:
- tens of thousands of tokens (common)
- hundreds of thousands (large)
- up to millions of tokens (very large, cutting-edge models)

> A useful mental reference: the complete works of Shakespeare are ~1 million tokens

Only a handful of modern models can process something that large in a single prompt.
If you are curious to explore and compare context windows and costs across models, a popular reference is the [Vellum leaderboard](https://www.vellum.ai/llm-leaderboard?utm_source=google&utm_medium=organic#compare),
which aggregates this information in a clear, visual way.


---

## ✅ Takeaway
The **context window** is not a minor technical detail.
>It is the operational boundary of what an LLM can reason about at inference time.

Understanding it makes: the illusion of memory disappear, token costs feel logical, and LLM behavior far more predictable.