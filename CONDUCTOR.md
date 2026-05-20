# LFM2/LFM2.5 — Conductor Context

This repo is the LFM-family training track for the Hermes Training Hub.

## Hub References

| Document | Location |
|---|---|
| Hub conductor | `/Users/doughnut/GitHub/hermes-training/CONDUCTOR.md` |
| Benchmark plan | `/Users/doughnut/GitHub/hermes-training/BENCHMARKING_PLAN.md` |
| Standard benchmarks | `/Users/doughnut/GitHub/hermes-training/STANDARD_BENCHMARKS.md` |
| Documentation plan | `/Users/doughnut/GitHub/hermes-training/DOCUMENTATION_PLAN.md` |
| Applications | `/Users/doughnut/GitHub/hermes-training/APPLICATIONS.md` |

## Track Status

| Requirement | Status |
|---|---|
| MLX LoRA pipeline | Passed smoke training |
| Dataset splits | Present: train/val/valid/test JSONL |
| Dataset token audit | LFM2.5 train split: 461 rows / 219,354 tokens |
| Adapter save path | Verified with LFM2.5 smoke adapter |
| Apple Silicon memory | LFM2.5 smoke peaked around 3.6 GB |
| SSD caching | Managed by hub `scripts/env.sh` |
| Evaluation | Seed eval exists; benchmark expansion required |
| Publishing | Adapter-only after benchmark promotion |

## Current Models

| Model | Role | Status |
|---|---|---|
| `LiquidAI/LFM2.5-1.2B-Instruct` | Low-latency Hermes helper / edge assistant | Smoke train passed |
| `LiquidAI/LFM2.5-1.2B-Thinking` | Reasoning helper candidate | Configured, not trained |
| `LiquidAI/LFM2-8B-A1B` | MoE-style runtime/fine-tune candidate | Configured, needs proof |
| `mlx-community/Ministral-3-8B-Instruct-2512-4bit` | Adjacent dense/edge baseline | Configured |
| `LiquidAI/LFM2-ColBERT-350M` | Retrieval/memory track candidate | Planned, use contrastive/retrieval evals not SFT |

## Proven Run

| Field | Value |
|---|---|
| Config | `scripts/train_config.lfm25-1.2b-instruct.smoke.yaml` |
| Iterations | 10 |
| Trained tokens | 5,462 |
| Peak memory | ~3.6 GB |
| Adapter | `experiments/lfm25-1.2b-instruct-smoke/lora_adapter` |
| Interpretation | Pipeline proof only, not quality proof |

## Next Actions

1. Run Hermes-local smoke evaluation on base vs smoke adapter.
2. Expand local eval set before making quality claims.
3. Run full-smoke-data training over the current 219k-token train split.
4. Add a run note with dataset audit, loss, memory, and benchmark output.
5. Only then decide whether to train LFM2.5-Thinking or move to Qwen3 4B.

## Contracts in Effect

- `data/raw/*.jsonl`: raw Hermes-style messages.
- `data/splits/*.jsonl`: train/val/valid/test split JSONL.
- `scripts/train_config*.yaml`: MLX LoRA config.
- `experiments/*/lora_adapter/`: ignored local adapter output.
- `eval/prompts.jsonl`: seed eval input, to be expanded.
- `modelfiles/*.Modelfile`: runtime packaging input.

## Application Notes

LFM-family models are best suited for:

- fast local Hermes helper model
- tool-routing and command-formatting assistant
- low-latency background summarizer
- privacy-preserving local workflow assistant
- retrieval companion when paired with LFM2-ColBERT

They should not be promoted as broad reasoning leaders until benchmarked against Qwen/Hermes/Gemma baselines.
