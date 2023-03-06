# 1. Funckcija mora da se zove test_area
# 2. 
import pytest
from functions import area


def test_area():
    assert area(5) == 25
    assert area(0) == 0
    assert area(10) == 100
    assert area(1.2) == 1.44


def test_negative_values():
    with pytest.raises(ValueError):
        area(-2)
