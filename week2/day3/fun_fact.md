# What are tokens, really? 🧩 
When we talk about **tokens**, we are really talking about *how text is represented* before being processed by a language model.  
At the very beginning of neural language models, text was handled **character by character**.  
The model would read one letter at a time and try to predict the next one. This approach had some nice properties:
> the vocabulary was tiny (letters, digits, punctuation), memory usage was low, and the system was conceptually simple.

However, it put too much burden on the neural network.
The model had to learn everything from scratch: how characters form words, how words relate to meaning, and how syntax emerges. Learning language structure at this level turned out to be very inefficient.

The next natural step was to move to **word-level models**.
Each input token was a full word. This made learning easier: words already carry semantic meaning, so the model could focus more on relationships between concepts.

But this introduced the opposite problem:
> human language contains an enormous number of possible words.
Proper names, technical terms, rare forms, and new words caused the vocabulary to explode.

To keep things manageable, rare words were often removed, which meant the model simply *could not understand or generate them*.

The real breakthrough came with a *middle-ground solution*:
instead of characters or full words, models started using subword units, what we now call *tokens*.  
A token can be:  
- a full word
- a part of a word (a prefix, a suffix, or a stem)
- sometimes even multiple short words combined

This approach keeps the vocabulary **limited and efficient**,
while still allowing the model to represent any word by falling back to smaller pieces when needed.  

>This compromise turned out to be extremely effective: models learn concepts faster, memory usage stays under control, inference is efficient, linguistic structure (like shared word stems) naturally emerges

### Note 📝
There is nothing *theoretically mandatory* about tokens. In principle, we could still use characters or full words. But in practice, tokenization is the sweet spot that works best for large-scale language models.


---

## 🔢 Tokens vs vectors (important distinction)
`Tokens are not vectors.`  
At the very beginning of the pipeline, the model receives **token IDs**: integers that uniquely identify each token in the vocabulary.
Only after that do these IDs get transformed into **vectors (embeddings)** inside the neural network.
So:
```text
Token → symbolic unit (represented by an ID)
Embedding → numerical vector learned by the model
```

This distinction is crucial and often confusing for beginners.

---

## 🔍 Want to see tokens in action?
We can inspect the [OpenAI tokenizer](https://platform.openai.com/tokenizer) and can see exactly how a piece of text is split into *tokens* and mapped to *token IDs*.
This is a great hands-on way to understand what the model actually sees when you type a sentence.

<p align="center">
  <img src="assets/tokenizer.png" alt="openai_tokenizer" width="400"/>
</p>

---

## 🧪 Try this in the tokenizer
Below are some example inputs you can paste into the [OpenAI tokenizer](https://platform.openai.com/tokenizer) 
interface and observe carefully how they are split into tokens.

### 1️⃣ Common words vs rare words
```text
This sentence contains only very common English words.
```
Most (or all) words are mapped one token per word. Now compare with:
```text
This sentence contains exquisitely handcrafted wizardry.
```
Here, less common words are split into **multiple subword tokens**, often reflecting meaningful fragments (stems, suffixes, endings).