# test_calculator.py
import calculator
import pytest

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_sub():
    assert calculator.sub(5, 3) == 2
    assert calculator.sub(0, 5) == -5

def test_mul():
    assert calculator.mul(3, 4) == 12
    assert calculator.mul(-2, 3) == -6

def test_div():
    assert calculator.div(10, 2) == 5
    assert calculator.div(7, 1) == 7

    with pytest.raises(ValueError):
        calculator.div(5, 0)