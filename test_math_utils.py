import pytest
from math_utils import add, subtract, multiply, divide, power, modulo

# --- ADD ---
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# --- SUBTRACT ---
@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-5, -5, 0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

# --- MULTIPLY ---
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-1, 5, -5),
    (0, 100, 0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

# --- DIVIDE ---
@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (-6, -2, 3),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

# --- POWER ---
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 8),
    (5, 0, 1),
    (3, 1, 3),
])
def test_power(a, b, expected):
    assert power(a, b) == expected

# --- MODULO ---
@pytest.mark.parametrize("a,b,expected", [
    (10, 3, 1),
    (5, 2, 1),
    (9, 3, 0),
])
def test_modulo(a, b, expected):
    assert modulo(a, b) == expected

def test_modulo_by_zero():
    with pytest.raises(ValueError, match="Cannot perform modulo with zero"):
        modulo(5, 0)

