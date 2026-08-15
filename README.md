# Nightly-actions
Github action pipeline


The project builds a nightly GitHub Actions pipeline that trains a PPO agent on CartPole‑v1 and enforces a reward threshold.
Successful runs freeze the trained policy and metrics into an immutable GHCR image for reproducible experiments.
A pinned experiment re‑evaluates the frozen policy using digest‑based container pulls.
The workflow outputs baseline vs experiment metrics to ensure stability and detect performance drift.
