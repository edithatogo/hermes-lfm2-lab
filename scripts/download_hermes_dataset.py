#!/usr/bin/env python3
"""Download and convert Hermes datasets for LFM2 training."""
import os
os.environ["HF_HOME"] = "/Volumes/PortableSSD/huggingface"
os.environ["HF_HUB_CACHE"] = "/Volumes/PortableSSD/huggingface/hub"
import json, sys
from pathlib import Path
from datasets import load_dataset

REPO_DIR = Path("/Users/doughnut/GitHub/hermes-training/lfm2")
RAW_DIR = REPO_DIR / "data/raw"

def download(name, output_file, max_samples=100):
    print(f"Downloading {name}...")
    ds = load_dataset(name, split="train", trust_remote_code=True)
    count = 0
    with open(output_file, "w") as f:
        for i, example in enumerate(ds):
            if max_samples and i >= max_samples:
                break
            if "messages" in example:
                example["id"] = f"lfm2-{count}"
                f.write(json.dumps({"id": example["id"], "messages": example["messages"]}) + "\n")
                count += 1
    print(f"  Wrote {count} conversations")
    return count

total = download("NousResearch/Hermes-3-Dataset", RAW_DIR / "hermes3.jsonl", 200)
total += download("NousResearch/hermes-function-calling-v1", RAW_DIR / "hermes_fc.jsonl", 100)
print(f"\nTotal: {total} conversations")

print("\nRunning dataset pipeline...")
ret = os.system(f"cd {REPO_DIR} && python3 scripts/build_dataset.py --input-dir data/raw --output-dir data/splits --dedup")
if ret == 0:
    for split in ["train", "val", "test"]:
        p = REPO_DIR / "data/splits" / f"{split}.jsonl"
        if p.exists():
            print(f"  {split}: {len(p.read_text().strip().splitlines())} conversations")