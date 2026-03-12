# ⚙️ Training-time vs Inference-time Scaling

## Training-time scaling
Training-time scaling means improving the model **during training** by increasing:
- model size (more parameters)
- training data
- compute used for training

Larger models generally learn better internal representations, which allows them to solve more complex problems.
Example:
```text
gpt-5-nano  → smaller model
gpt-5-mini  → larger model
```
A larger model can sometimes solve a problem even with **minimal reasoning effort**.

---

## Inference-time scaling

Inference-time scaling means improving performance **after training**, by allowing the model to spend more compute while generating the answer.

With the GPT-5 models this can be controlled using the parameter `reasoning_effort` with four possible values:
```text
minimal
low
medium
high
```
where Higher reasoning effort means the model spends **more internal reasoning steps** before producing the answer.

---