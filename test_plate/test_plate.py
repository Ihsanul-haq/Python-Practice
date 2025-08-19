from test_plate.plate import is_valid
import pytest

def test_letters():
    assert is_valid("Ih") == True
    assert is_valid("I") == False
    assert is_valid("Ihsanul") == False

def test_alpha():
    assert is_valid("i1") == False
    assert is_valid("11") == False
    assert is_valid("il") == True

def test_alnum():
    assert is_valid("ihsan1") == True
    assert is_valid("ihs1 ") == False
    assert is_valid("iih89_") == False
def test_digit():
    assert is_valid("ihsa0") == False
    assert is_valid("ihs1t") == False
    assert is_valid("CS50") == True