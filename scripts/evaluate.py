#!/usr/bin/env python3
"""
Evaluate the fine-tuned model on a set of prompts.
"""
import argparse
import json
import sys
from pathlib import Path

def load_prompts(filepath: Path):
    """Load prompts from a JSONL file."""
    prompts = []
    with filepath.open('r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line.strip())
            prompts.append(data.get('prompt', ''))
    return prompts

def stub_generate(prompt: str, model_path: str) -> str:
    """Stub generation function. Replace with real model inference."""
    # In a real scenario, we would load the model and generate.
    return f"[Eval stub for {model_path}] {prompt[:50]}..."

def main():
    parser = argparse.ArgumentParser(description="Evaluate a model on prompts.")
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Path to the model or adapter."
    )
    parser.add_argument(
        "--prompts",
        type=Path,
        required=True,
        help="Path to JSONL file containing prompts."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("eval_results.jsonl"),
        help="Path to save results."
    )
    args = parser.parse_args()

    prompts = load_prompts(args.prompts)
    results = []
    for prompt in prompts:
        response = stub_generate(prompt, args.model)
        results.append({
            "prompt": prompt,
            "model": args.model,
            "response": response
        })

    with args.output.open('w', encoding='utf-8') as f:
        for res in results:
            f.write(json.dumps(res) + "\n")

    print(f"Saved {len(results)} results to {args.output}")
    return 0

if __name__ == "__main__":
    sys.exit(main())