# Contributing to hermes-lfm2-lab

Contributions improve the LFM-family model-training track for the Hermes Training Hub, including datasets, training configurations, evaluation, and runtime packaging inputs.

## Before you start

Read the [README](README.md) and [Conductor context](CONDUCTOR.md). Identify the affected model family and existing track before proposing new training or packaging work. Follow the hub benchmark and documentation requirements referenced there.

Search existing issues and pull requests to avoid duplicating work. Describe substantial proposals before implementation, and use repository issue or pull request templates when available. Small corrections can go directly into a focused pull request.

For bug reports, include the affected version or commit, environment, minimal reproduction, expected and actual behavior, and sanitized diagnostics. For feature requests, explain the use case and intended outcome.

## Development and validation

Use the appropriate checked-in configuration rather than assuming all LFM, LFM2.5, or adjacent baseline models share an architecture or objective. Record model revision, dataset and split provenance, token counts, environment, resource limits, and exact training/evaluation invocations.

Treat a smoke-training result as pipeline evidence. Compare base and adapted models on held-out evaluation before making quality claims or recommending promotion. Retrieval-model changes require retrieval-appropriate objectives and evaluation, as specified in the Conductor context; ordinary chat fine-tuning evidence is not interchangeable.

Keep local adapters, caches, and large generated artifacts outside Git. Preserve the existing adapter-only publication and benchmark-promotion conditions. Where the required hardware or runtime is unavailable, state the unexecuted check instead of transferring a result from another model or platform.

Update affected documentation and examples alongside behavior changes. Add a focused regression case for a bug fix where executable tests are appropriate. Record checks that were not run and the reason.

## Submitting a pull request

Create a focused branch from the current `main` branch and open a pull request back to it. Keep unrelated formatting, refactoring, and dependency changes separate.

Include:

- The problem, proposed change, and resulting behavior.
- Related issues or existing track references.
- Exact validation commands or inspection steps, results, and limitations.
- Compatibility implications and any data or dependency provenance.

Inspect the complete diff before submission. Required automated checks must pass before merge. Follow the existing repository and account policies; this guide does not introduce a second-person approval requirement or relax existing checks.

## Security and sensitive information

Follow the [account security policy](https://github.com/edithatogo/.github/blob/main/SECURITY.md). Report vulnerabilities privately through GitHub's **Report a vulnerability** option if available. Otherwise request a private reporting contact without disclosing the vulnerability publicly. Keep credentials, personal data, and unredacted logs out of commits, issues, and examples.

## Licensing and conduct

Preserve existing attribution and applicable source or package terms. This guide does not grant a new license. Submit only material you are entitled to contribute, and document unclear permissions before adding third-party content. Follow the [account code of conduct](https://github.com/edithatogo/.github/blob/main/CODE_OF_CONDUCT.md). This guide adds no CLA, mandatory sign-off, or relicensing condition.

## Reference guidance

- [GitHub contributor guidelines](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)
- [OpenSSF Best Practices criteria](https://www.bestpractices.dev/en/criteria)
