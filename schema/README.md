# schema/

Single physical location for nutrient definitions, VLM prompts, the VLM output schema, code generation and the evaluation set (PRD §8). Dart and Python code is generated from here; never write a second copy of these definitions by hand.

| Path | Content | Task |
| --- | --- | --- |
| `nutrients.yaml` | Nutrient keys, units, German label order, parent lines, OFF mapping | C-1 |
| `nutriscan_schema/` | Pydantic models for the VLM output | C-2 |
| `eval/models.yaml` | Model IDs, prices and image limits (single source of truth) | C-3 |
| `codegen/`, `generated/` | Code generation and its outputs (never edited by hand) | C-4 |
| `prompts/` | Versioned VLM prompts; frozen once they have produced data | P05-3 |
| `eval/` | Evaluation photos, ground truth and the evaluation script | P0-4, P0-5, P05-4 |

Everything in `nutrients.yaml`, `nutriscan_schema/` and `eval/models.yaml` is a **shared contract**: change it only in a dedicated PR (CONTRIBUTING §2).
