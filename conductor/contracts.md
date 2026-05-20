# Contracts — LFM2 Track

## LFM-DATA-001

Training data must use chat JSONL with `messages` and must provide `train`, `val`, `valid`, and `test` splits.

## LFM-TRAIN-001

Training configs must include `model`, `adapter_path`, `data`, LoRA parameters, iteration count, and max sequence length.

## LFM-ART-001

Adapters must save under ignored `experiments/` paths and contain `adapters.safetensors` plus `adapter_config.json`.

## LFM-HEALTH-001

The track cannot be marked complete until health is estimated at `>= 9.5 / 10`.
