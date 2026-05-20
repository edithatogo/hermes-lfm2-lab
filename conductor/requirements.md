# Requirements — LFM2 Track

## Must Have

| ID | Requirement | Verification |
|---|---|---|
| M1 | LFM2.5 smoke adapter can be reproduced | smoke config trains and saves adapter |
| M2 | Full-smoke-data config over current dataset | dry-run passes |
| M3 | Dataset audit recorded before training claims | `dataset_token_audit.py` output included |
| M4 | Base vs adapter evaluation | comparison output exists |
| M5 | Health >= 9.5 before completion | health checkpoint in plan |

## Should Have

| ID | Requirement | Priority |
|---|---|---|
| S1 | LFM2.5-Thinking follow-up config | Medium |
| S2 | LFM2-ColBERT retrieval track proposal | Medium |
| S3 | Run-card template for LFM runs | High |

## Won't Have

| ID | Requirement | Reason |
|---|---|
| W1 | Publish smoke adapter as quality model | insufficient trained tokens |
