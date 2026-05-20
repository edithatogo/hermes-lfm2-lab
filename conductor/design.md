# Design — LFM2 Track

```mermaid
flowchart LR
    ENV[../scripts/env.sh] --> CACHE[(SSD cache)]
    SPLITS[data/splits] --> AUDIT[dataset token audit]
    SPLITS --> TRAIN[train.py]
    CACHE --> TRAIN
    TRAIN --> ADAPTER[experiments/lfm25*/lora_adapter]
    ADAPTER --> EVAL[evaluate.py / compare.py]
    EVAL --> HEALTH[health >= 9.5 gate]
```

LFM2.5 training is optimized for low memory and fast local iteration. Retrieval work such as LFM2-ColBERT should use a separate contrastive/retrieval plan rather than chat SFT.
