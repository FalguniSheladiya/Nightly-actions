FROM ghcr.io/falgunisheladiya/nightly-actions/rl-base:latest

WORKDIR /app

COPY src/ src/
COPY pyproject.toml .
COPY out/policy.zip out/policy.zip
COPY out/metrics.json out/metrics.json

ENV PYTHONPATH=/app

LABEL org.opencontainers.image.source="https://github.com/<owner>/<repo>"
LABEL org.opencontainers.image.revision="${GIT_SHA}"
LABEL org.opencontainers.image.created="${CREATED_AT}"

ENTRYPOINT ["python", "-m", "src.evaluate"]
