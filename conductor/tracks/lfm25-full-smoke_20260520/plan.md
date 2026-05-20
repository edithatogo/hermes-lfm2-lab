# Plan: LFM2.5 Full-Smoke-Data

## Phase 1: Prepare

- [x] Task: Create full-smoke-data config.
- [x] Task: Audit dataset token count and truncation.
- [x] Task: Dry-run config.

## Phase 2: Train

- [x] Task: Run full-smoke-data training.
- [x] Task: Save adapter and run note.

## Phase 3: Evaluate

- [x] Task: Run base vs adapter evaluation.
- [x] Task: Update hub docs with result.

## Health Check

- Current estimate: 9.6 / 10
- Evidence: full-smoke training completed for 200 iterations / 175,895 trained tokens with final validation loss 1.455, peak memory 6.022 GB, and elapsed time 334.3 seconds. Base and adapter evaluations completed on 100 Hermes-local prompts and are summarized in `eval/lfm25-full-smoke-summary.md`.
- Decision: the adapter is a valid load/evaluation proof but not a publication candidate because it collapses to empty or near-empty responses.
- Gaps: the next safer training recipe remains outside this completed proof track.
- [x] Task: Estimate track health using hub `conductor/health-score.md`.
- [x] Task: Close or document all gaps below health 9.5.
- [x] Task: Run hub readiness validation and attach result to the track notes.
- [x] Task: Confirm health >= 9.5 before marking this track complete.
