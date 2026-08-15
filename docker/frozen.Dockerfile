FROM ghcr.io/falgunisheladiya/nightly-actions/rl-base:nightly

WORKDIR /app

COPY src/ src/
COPY pyproject.toml .

COPY out/policy.zip policy.zip
COPY out/metrics.json metrics.json

ENV PYTHONPATH=/app

ENTRYPOINT ["python", "-m", "src.evaluate"]
