#TDD practice with math utils
from math_utils import is_even, factorial, find_max,is_prime 
import pytest

def test_is_even():
  assert is_even(2) == True
  assert is_even(3) == False
  assert is_even(0) == True
  assert is_even(-2) == True

def test_factorial():
  assert factorial(0) == 1
  assert factorial(1) == 1
  assert factorial(5) == 120
  with pytest.raises(ValueError):
    factorial(-1)

def test_find_max():
  assert find_max([1, 2, 3]) == 3
  assert find_max([5, 2, 1, 8]) == 8
  assert find_max([-1, -5, -3]) == -1
  with pytest.raises(ValueError):
    assert find_max([])

def test_is_prime():
  assert is_prime(2) == True
  assert is_prime(3) == True
  assert is_prime(4) == False
  assert is_prime(17) == True
  assert is_prime(1) == False
  with pytest.raises(ValueError):
      is_prime(-5)