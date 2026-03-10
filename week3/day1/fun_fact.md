# ✨ What Kind of Data Do LLMs Understand Best?

Large Language Models are trained on **massive datasets collected from the web**.  
Because of this, they become extremely familiar with certain **types of textual structures**.

Three formats appear very frequently in their training data:

1. Natural language  
2. Markdown  
3. JSON  

Understanding this helps explain **why some prompts work better than others**.

---

# 1️⃣ Natural Language

The majority of the data used to train LLMs consists of **plain human language**:

- books
- articles
- forums
- documentation
- conversations

Because of this, LLMs are very good at tasks such as:

- answering questions
- summarizing text
- explaining concepts
- generating descriptions

---

# 2️⃣ Markdown
A surprisingly important format for LLMs is **Markdown**.  
Most documentation, blogs, and technical content on the web is written in Markdown or converted to it during preprocessing.

As a result, LLMs are extremely familiar with its structure.

Markdown is essentially a **lightweight version of HTML** used to format text.

LLMs are particularly good at generating: headings, lists, tables, formatted documentation.

That is why Markdown is often used when generating:
- README files
- documentation
- structured reports

---

# 3️⃣ JSON
LLMs are also trained on large amounts of structured data, especially **JSON**.

JSON (JavaScript Object Notation) is commonly used in: APIs, configuration files, web applications, and datasets.

Because models see JSON frequently, they are good at understanding and generating structured information in this format.


---

## Why Structured Formats Matter
When interacting with LLMs, the format of the data strongly influences the output.

| Format           | Strength                         |
| ---------------- | -------------------------------- |
| Natural language | explanations, conversations      |
| Markdown         | structured documents             |
| JSON             | machine-readable structured data |

---

## ⭐️ Bonus — A New Format for LLMs: TOON

Recently, researchers and developers started experimenting with a new data format called **TOON (Token-Oriented Object Notation)**.

TOON is designed specifically for **Large Language Models**.

The motivation is simple: **JSON is very verbose for LLMs**.

Every symbol in JSON — quotes, commas, brackets — consumes tokens.  
When large datasets are included in prompts, this can significantly increase cost and context usage.

TOON removes most of this syntactic overhead while keeping the same structure.

### JSON example

```json
{
 "users": [
  {"id": 1, "name": "Alice", "role": "admin"},
  {"id": 2, "name": "Bob", "role": "user"}
 ]
}
```

### TOON Equivalent
```text
users[2]{id,name,role}:
1,Alice,admin
2,Bob,user
```

Field names are declared once, and each row represents a record.
This approach can reduce token usage by 30–60%, making prompts more efficient when sending structured data to LLMs.
In practice, many systems still use JSON internally but convert it to TOON when interacting with the model.

---

## When NOT to Use TOON

TOON is **not meant to replace JSON**.

JSON remains the better choice for:

- APIs  
- communication between services  
- data storage  
- deeply nested data structures  

In practice, many developers follow a hybrid workflow:
```text
Application → JSON → convert to TOON → send to LLM
LLM response → convert back to JSON
```

In this setup, **TOON acts as an interface format for interacting with the LLM**, while JSON remains the standard format used by the application.