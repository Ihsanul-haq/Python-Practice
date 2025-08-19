from test_fuel.fuel import convert, gauge
import pytest
def test_fraction():
    assert convert("3/4") == 75
    assert convert("2/2") == 100
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("2/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(75) == "75 %"

    
    