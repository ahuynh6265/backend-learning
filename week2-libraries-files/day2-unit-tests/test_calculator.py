import pytest

from calculator import add, subtract, multiply, divide, exponent

def test_add():
  assert add(2, 5) == 7
  assert add(-1, 1) == 0
  assert add(0, 0) == 0

def test_subtract():
  assert subtract(5, 2) == 3
  assert subtract(5, 5) == 0
  assert subtract(0, -4) == 4

def test_multiply():
  assert multiply(2, 5) == 10
  assert multiply(0, 100) == 0
  assert multiply(-4, 5) == -20

def test_divide():
  assert divide(10, 2) == 5
  assert divide(-6, 2) == -3

def test_divide_by_zero():
  with pytest.raises(ValueError):
    divide(10, 0)

def test_exponent():
  assert exponent(10) == 100
  assert exponent(0) == 0
  assert exponent(-4) == 16

