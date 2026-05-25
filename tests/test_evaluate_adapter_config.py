from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.evaluate import ensure_mlx_adapter_config


class EvaluateAdapterConfigTests(unittest.TestCase):
    def test_old_lora_config_is_upgraded_for_current_mlx_loader(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            adapter = Path(tmp)
            config_path = adapter / "adapter_config.json"
            config_path.write_text(
                json.dumps(
                    {
                        "model": "LiquidAI/LFM2.5-1.2B-Instruct",
                        "lora_rank": 8,
                        "lora_scale": 16.0,
                        "lora_dropout": 0.0,
                        "lora_layers": 8,
                    }
                )
                + "\n",
                encoding="utf-8",
            )

            ensure_mlx_adapter_config(str(adapter))
            upgraded = json.loads(config_path.read_text(encoding="utf-8"))

            self.assertEqual(upgraded["fine_tune_type"], "lora")
            self.assertEqual(upgraded["num_layers"], 8)
            self.assertEqual(upgraded["lora_parameters"], {"rank": 8, "scale": 16.0, "dropout": 0.0})

    def test_current_config_is_left_unchanged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            adapter = Path(tmp)
            config_path = adapter / "adapter_config.json"
            original = {
                "fine_tune_type": "lora",
                "num_layers": 16,
                "lora_parameters": {"rank": 16, "scale": 20.0, "dropout": 0.0},
            }
            config_path.write_text(json.dumps(original, indent=2) + "\n", encoding="utf-8")

            ensure_mlx_adapter_config(str(adapter))

            self.assertEqual(json.loads(config_path.read_text(encoding="utf-8")), original)


if __name__ == "__main__":
    unittest.main()
