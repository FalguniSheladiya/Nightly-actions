import math, subprocess
from datetime import datetime, timezone

def mean_std(values: list[float]) -> tuple[float, float]:
    if not values:
        raise ValueError("mean_std() requires at least one value")
    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    return mean, math.sqrt(variance)

def git_sha() -> str:
    try:
        out = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, check=True)
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")
