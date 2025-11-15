from grade_calculator import calculate_grade, get_gpa, calculate_gpa
import pytest

#Tests for grades first 
def test_grade_function():
  assert calculate_grade(100) == "A"
  assert calculate_grade(90) == "A"
  assert calculate_grade(89) == "B"
  assert calculate_grade(79) == "C"
  assert calculate_grade(69) == "D"
  assert calculate_grade(59) == "F"
  assert calculate_grade(0) == "F"

def test_grade_too_low():
  with pytest.raises(ValueError):
    calculate_grade(-1)

def test_grade_too_high():
  with pytest.raises(ValueError):
    calculate_grade(101)

#Tests for gpa
def test_gpa_function():
  assert get_gpa('A') == 4.0
  assert get_gpa('B') == 3.0
  assert get_gpa('C') == 2.0
  assert get_gpa('D') == 1.0
  assert get_gpa('F') == 0

#tests for gpa calculation 
def test_single_gpa():
  assert calculate_gpa(['A']) == 4.0
  assert calculate_gpa(['B']) == 3.0

def test_multiple_gpa():
  assert calculate_gpa(['A', 'B', 'C', 'D', 'F']) == 2.0
  assert calculate_gpa(['A', 'B']) == 3.5

def test_duplicates_gpa():
  assert calculate_gpa(['A', 'A', 'B']) == (4.0 + 4.0 + 3.0)/3
  assert calculate_gpa(['B', 'B', 'D']) == (3.0 + 3.0 + 1.0)/3

def test_all_same():
  assert calculate_gpa(['A', 'A']) == 4.0
  assert calculate_gpa(['F', 'F']) == 0

def test_empty():
  with pytest.raises(ValueError):
    assert calculate_gpa([])










  
  