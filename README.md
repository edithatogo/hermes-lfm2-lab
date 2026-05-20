# Hermes LFM Lab

Training and packaging workspace for LFM/LFM2-family Hermes-style fine-tunes.

Status: scaffolded, with LFM2 default and Ministral as an adjacent 8B edge-model experiment.

Smoke proof: `LiquidAI/LFM2.5-1.2B-Instruct` completed a 10-iteration MLX LoRA run on the MacBook Pro M1 Max target and saved a local adapter under `experiments/lfm25-1.2b-instruct-smoke/lora_adapter`.

Folder structure:
- data/raw/ — raw collected conversations
- data/clean/ — cleaned, deduped conversations
- data/splits/ — train/val/test splits in JSONL
- experiments/lfm2-8b-a1b/ — LFM2 MLX LoRA training outputs
- experiments/ministral-8b/ — Ministral MLX LoRA training outputs
- eval/ — evaluation prompts and results
- exports/hf/ — artifacts for Hugging Face publishing
- scripts/ — helper scripts for dataset, training, eval, export
- modelfiles/ — Ollama Modelfile(s)

Configs:

- `scripts/train_config.yaml` — LiquidAI/LFM2-8B-A1B default.
- `scripts/train_config.lfm25-1.2b-instruct.smoke.yaml` — 10-iteration LFM2.5 proof run.
- `scripts/train_config.lfm25-1.2b-instruct.yaml` — LFM2.5 low-latency instruct target.
- `scripts/train_config.lfm25-1.2b-thinking.yaml` — LFM2.5 low-latency reasoning target.
- `scripts/train_config.ministral.yaml` — Ministral 3 8B experiment.

Runtime targets:

- Ollama/GGUF for broad use and LM Studio compatibility.
- Ollama experimental safetensors when local architecture support passes a smoke test.
- Hermes through `ollama launch hermes`.
