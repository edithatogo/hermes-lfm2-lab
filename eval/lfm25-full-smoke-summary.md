# LFM2.5 Full-Smoke Evaluation Summary

Date: 2026-05-21

## Run

- Base model: `LiquidAI/LFM2.5-1.2B-Instruct`
- Adapter: `experiments/lfm25-1.2b-instruct-full-smoke/lora_adapter`
- Training config: `scripts/train_config.lfm25-1.2b-instruct.full-smoke.yaml`
- Prompt set: `eval/prompts.jsonl`
- Prompt count: 100
- Max generation tokens: 128
- Storage environment: `HERMES_STORAGE_ROOT=/Volumes/PortableSSD`, `HF_HOME=/Volumes/PortableSSD/huggingface`, `TMPDIR=/Volumes/PortableSSD/tmp`

## Training Result

- Iterations: 200
- Trained tokens: 175,895
- Final train loss: 1.784
- Final validation loss: 1.455
- Peak memory: 6.022 GB
- Elapsed time: 334.3 seconds
- Adapter weights: `experiments/lfm25-1.2b-instruct-full-smoke/lora_adapter/adapters.safetensors`

## Evaluation Commands

```bash
source scripts/env.sh
cd lfm2
../.venv/bin/python scripts/evaluate.py \
  --model LiquidAI/LFM2.5-1.2B-Instruct \
  --prompts eval/prompts.jsonl \
  --output eval/lfm25-base-results.jsonl \
  --report eval/lfm25-base-report.html \
  --max-tokens 128

../.venv/bin/python scripts/evaluate.py \
  --model LiquidAI/LFM2.5-1.2B-Instruct \
  --adapter experiments/lfm25-1.2b-instruct-full-smoke/lora_adapter \
  --prompts eval/prompts.jsonl \
  --output eval/lfm25-full-smoke-adapter-results.jsonl \
  --report eval/lfm25-full-smoke-adapter-report.html \
  --max-tokens 128
```

## Metrics

| Model | Prompts | Avg Latency | Avg Response Length |
|---|---:|---:|---:|
| Base | 100 | 0.897s | 63.18 words |
| Full-smoke adapter | 100 | 0.221s | 4.32 words |

Category-level average response lengths:

| Category | Base Words | Adapter Words |
|---|---:|---:|
| tool_use | 60.92 | 5.28 |
| code | 71.20 | 9.25 |
| long_context | 74.73 | 0.00 |
| reasoning | 75.67 | 6.20 |
| safety | 58.60 | 1.10 |
| factual | 42.60 | 0.00 |
| formatting | 20.60 | 2.20 |

## Response Gate

Command:

```bash
source scripts/env.sh
./.venv/bin/python scripts/eval_response_gate.py \
  lfm2/eval/lfm25-full-smoke-adapter-results.jsonl
```

Result:

- Base output passes the response-collapse gate with `avg_words=63.18` and `empty_rate=0.100`.
- Full-smoke adapter fails with `avg_words=4.32` and `empty_rate=0.840`.

## Decision

The adapter is a valid runtime/load proof after adding MLX-compatible adapter metadata, but it is not publishable. The near-empty outputs indicate the current full-smoke training recipe overfits or otherwise collapses response generation.

Next training iteration should reduce risk before scaling:

- lower the learning rate from `1e-4`
- add a short eval checkpoint after 25-50 iterations
- compare `lora_layers` and rank settings before longer runs
- add an automatic empty-response and response-length gate to evaluation
