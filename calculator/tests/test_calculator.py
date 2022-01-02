import pytest
from calculator.calculator import add, subtract, multiply, divide

@pytest.mark.parametrize('a,b,expected', [(3, 5, 8), (1, 1, 2), (-52, 5, -47999)])
def test_add_two_int(a, b, expected):    
    assert add(a, b) == expected
    
@pytest.mark.parametrize('a,b,expected', [(7, 5, 2), (2, 1, 1), (1, 99, -98)])
def test_subtract_two_int(a, b, expected):    
    assert subtract(a, b) == expected
    
@pytest.mark.parametrize('a,b,expected', [(5, 7, 35), (4, 3, 12), (-6, 8, -48)])
def test_multiply_two_int(a, b, expected):    
    assert multiply(a, b) == expected

@pytest.mark.parametrize('a,b,expected', [(5, 1, 5), (1024, 5, 204.8), (36, -3, -12)])
def test_divide_two_int(a, b, expected):    
    assert divide(a, b) == expected