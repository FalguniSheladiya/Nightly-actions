FROM python:3.11-slim

WORKDIR /app

# Install system dependencies required by gymnasium
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
       gymnasium==0.29.1 \
       stable-baselines3==2.3.0 \
       torch --index-url https://download.pytorch.org/whl/cpu \
       pytest

COPY pyproject.toml .
COPY src/ src/
COPY tests/ tests/

ENV PYTHONPATH=/app

CMD ["python", "-m", "src.train"]
