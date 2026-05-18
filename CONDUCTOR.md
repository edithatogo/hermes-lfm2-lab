# LFM2 — Conductor Setup

This repo is Track 2 of the Hermes Training Hub.

## Hub References

| Document | Location |
|----------|----------|
| Hub conductor | `/Users/doughnut/GitHub/hermes-training/CONDUCTOR.md` |
| MoSCoW requirements | `/Users/doughnut/GitHub/hermes-training/REQUIREMENTS.md` |
| Architecture design | `/Users/doughnut/GitHub/hermes-training/DESIGN.md` |
| Interface contracts | `/Users/doughnut/GitHub/hermes-training/CONTRACTS.md` |

## Track Status

| Requirement | Status |
|-------------|--------|
| M1 MLX LoRA pipeline | ✅ scripts copied from gemma4 template |
| M2 Download dataset | 🔄 download_hermes_dataset.py running |
| M3 Train on Hermes data | 📋 Planned (after gemma4 pipeline proven) |
| M4 Save adapter | 📋 Planned |
| M8 Dataset dedup | ✅ build_dataset.py tested on sample data |
| M9 Apple Silicon MLX | ✅ mlx + mlx-lm installed |
| M10 SSD caching | ✅ HF_HOME=/Volumes/PortableSSD/... |
| S1 Eval comparison | ✅ scripts/evaluate.py + compare.py copied |
| S3 HF publishing | ✅ scripts/push_to_hf.sh adapted for LFM2 |

## Active Processes

| Process | PID | What |
|---------|-----|------|
| proc_2d4febbe46bc | 40038 | Hermes dataset download (LFM2) |
| proc_21b478290568 | 43197 | LFM2 model pre-download to SSD cache |

## Key Differences from Gemma 4

| Aspect | Gemma 4 | Ministral 3 8B (replaces LFM2) |
|--------|---------|-------------------------------|
| Model size | 4B (all active) | 8B |
| License | Apache 2.0 | Apache 2.0 |
| Chat template | `<\|start_header_id\|>` ... `<\|eot_id\|>` | `[INST]` ... `[/INST]` |
| Modelfile | `modelfiles/Gemma4-Hermes.Modelfile` | `modelfiles/Ministral-Hermes.Modelfile` |
| Training config | `scripts/train_config.yaml` (G4 config) | `scripts/train_config.yaml` (Ministral config) |

**Note:** Originally scaffolded for LFM2-8B-A1B but that model has restricted access.
Switched to Ministral 3 8B (Apache 2.0, well-supported).

## Contracts in Effect

Same contract set as gemma4 (CONTRACT-001 through CONTRACT-008), with track-specific overrides:
- CONTRACT-003: LFM2-specific `train_config.yaml`
- CONTRACT-006: `modelfiles/LFM2-Hermes.Modelfile`
- CONTRACT-004: `experiments/lfm2-8b-a1b/lora_adapter/`

## Context Preservation Notes

When working here:
- This repo is BLOCKED on gemma4 pipeline completion (we want to prove the pipeline first)
- The LFM2-8B-A1B model is MoE — only 1B parameters active per forward pass
- Despite 8B total params, training memory is closer to a 1B-2B dense model
- License restrictions may prevent uploading full weights to HF — publish adapter only
