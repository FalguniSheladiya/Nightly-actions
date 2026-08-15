# Nightly-actions
Github action pipeline

Pipeline Design Overview

This project implements a four‑stage reinforcement‑learning pipeline that runs nightly on GitHub Actions. Each stage depends strictly on the previous one, forming a linear chain that guarantees correctness, reproducibility, and isolation of results. The base image is built first, providing a controlled environment with fixed versions of Gymnasium, Stable‑Baselines3, PyTorch, and evaluation tools. The training + gate stage runs inside that image and produces the policy and baseline metrics; if the trained agent fails to meet the reward threshold, the entire workflow stops. Only successful training artifacts are passed forward. The freeze stage then embeds the trained policy, metrics and evaluation code into a self‑contained container image. Finally, the pinned experiment stage pulls that frozen image by digest and re‑evaluates the policy under new conditions, comparing experiment metrics against the frozen baseline.

The idea of a frozen image is central to the design. A frozen image guarantees that everything inside it is immutable: the policy, the evaluation code, the dependencies, and the baseline metrics. Nothing inside the image can drift between runs, and nothing external can influence its behavior. This ensures that any experiment using the frozen image starts from a perfectly preserved snapshot of the successful nightly training run.

However, only the digest guarantees immutability across time. Tags like `nightly` or `latest` can move, but a digest cannot. Pulling the frozen image using its digest ensures that the experiment stage always uses the exact binary content produced by the freeze stage — not a later rebuild, not a retagged version, and not a modified image. Digest‑pinning is the strongest reproducibility guarantee available in containerized ML workflows.

With more time, I would extend the pipeline to track performance drift across multiple environments and visualize nightly trends. This would turn the workflow from a reproducibility mechanism into a monitoring system that detects regressions, instability or unexpected changes in agent behavior over time.
