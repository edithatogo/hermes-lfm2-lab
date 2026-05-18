---
license: other
library_name: mlx
tags:
- hermes
- lfm
- lfm2
- lora
- fine-tune
- instruction-tuning
base_model: LiquidAI/LFM2-8B-A1B
datasets:
- NousResearch/Hermes-3-Dataset
- NousResearch/hermes-function-calling-v1
language:
- en
pipeline_tag: text-generation
---

# LFM2 Hermes — LoRA Adapter

Adapter-only Hermes-style fine-tune for the LFM/LFM2 track.

## Training Details

- **Default base model:** LiquidAI/LFM2-8B-A1B
- **Method:** LoRA
- **Framework:** Apple MLX when supported; GGUF/Ollama runtime validation required
- **Hardware target:** MacBook Pro M1 Max, 32GB RAM
- **Dataset:** Hermes-3-Dataset + hermes-function-calling-v1

## Runtime Notes

Use the exact base model revision recorded in `adapter_config.json`.
For Hermes, prefer serving through Ollama and launching with:

```bash
ollama launch hermes
```

This release is adapter-only. Verify the base model license before publishing merged weights.
