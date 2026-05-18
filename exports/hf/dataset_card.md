---
license: apache-2.0
task_categories:
- text-generation
language:
- en
tags:
- hermes
- instruction-tuning
- tool-use
- fine-tuning
---

# Hermes-Style Training Data

Shared JSONL dataset for Hermes-style supervised fine-tuning.

Each row has:

```json
{"id":"example-id","messages":[{"role":"user","content":"..."},{"role":"assistant","content":"..."}]}
```

Sources:

- NousResearch/Hermes-3-Dataset
- NousResearch/hermes-function-calling-v1

The dataset is deduplicated by conversation hash and split into train/val/test.
