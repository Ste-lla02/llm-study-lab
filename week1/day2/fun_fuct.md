# Fun fact ✨ – Prompt, Completion, and Inference 📖

When working with Large Language Models, it is useful to clarify some fundamental terminology.

The **text you provide to a language model** is called a **prompt**.  
The prompt represents the input and defines what the model should respond to.

Once the prompt is given, the model generates an answer.  
The **result produced by the model** is known as a **completion**.

The entire process of using a model to generate text from a prompt is called **inference**.

---

## Prompt: why is it called that?
In English, prompt means stimulus, trigger, or something that induces an action.
From the perspective of language models:  
- the prompt is everything you provide as input to the model
- it is not just a “question”, but a sequence of tokens that initializes a probability distribution

Why not simply call it input?
- because the prompt is not neutral
- its structure, wording, and context actively guide the model’s behavior
- it may include instructions, examples, tone, and constraints → prompt engineering

---
## Completion: why not “output”?

Completion literally means finishing or continuing something.
This term is conceptually very important.
A language model does not answer questions in the traditional sense:  
- it continues a text sequence
- it generates tokens that are probabilistically consistent with the prompt

> From the model’s point of view the prompt is a prefix and the response is a plausible continuation.

---
## 3. Inference: why this term is crucial

In machine learning:
- training → the model’s parameters are updated
- inference → the parameters are fixed and the model is simply used  

It means that the model has already been trained, it is not learning anything new, and it is only performing a forward pass through the neural network.  

More concretely:
1. the prompt is tokenized
2. passed through the transformer
3. the model produces a probability distribution over next tokens
4. one token is selected or sampled
5. the process repeats (autoregressively)  
> All of this is inference, not training.


---
## Why this distinction matters

Understanding the difference between prompt, completion, and inference helps to:
- reason more clearly about how language models work,
- design better prompts,
- interpret model outputs correctly,
- avoid treating the model as a black box.

In practice:
- the **prompt** is what we control,
- the **completion** is what we observe,
- **inference** is the mechanism that connects the two.

These concepts form the foundation of any interaction with generative language models.
