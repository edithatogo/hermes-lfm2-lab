# Hermes LFM2 Lab

Training and packaging workspace for LFM2-8B-A1B Hermes-style finetune.

Status: scaffolded

Folder structure:
- data/raw/ — raw collected conversations
- data/clean/ — cleaned, deduped conversations
- data/splits/ — train/val/test splits in JSONL
- experiments/lfm2-8b-a1b/ — MLX LoRA training outputs
- eval/ — evaluation prompts and results
- exports/hf/ — artifacts for Hugging Face publishing
- scripts/ — helper scripts for dataset, training, eval, export
- modelfiles/ — Ollama Modelfile(s)

Next steps as of 2026-05-16:
- Gemma 4 first-pass training is downloading/running
- LFM2 repo is scaffolded and ready for the same pipeline
