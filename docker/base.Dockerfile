FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
       gymnasium>=0.29 \
       stable-baselines3>=2.3 \
       --index-url https://download.pytorch.org/whl/cpu \
       torch \
       pytest

COPY pyproject.toml .
COPY src/ src/
COPY tests/ tests/

ENV PYTHONPATH=/app

CMD ["python", "-m src.train"]
