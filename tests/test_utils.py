import pytest
from src.utils import mean_std, utc_now_iso

def test_mean_std_basic():
    mean, std = mean_std([1.0, 2.0, 3.0])
    assert mean == pytest.approx(2.0)
    assert std == pytest.approx(0.8164965809)

def test_mean_std_empty_raises():
    with pytest.raises(ValueError):
        mean_std([])

def test_utc_now_iso_has_timezone():
    assert utc_now_iso().endswith("+00:00")
