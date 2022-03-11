import pytest
from main import fizzbuzz

def test_3_returns_fizz():
    assert fizzbuzz(3) == "fizz", "3 should return fizz"
def test_5_returns_buzz():
    assert fizzbuzz(5) == "buzz", "5 should return buzz"
def test_15_returns_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz", "15 should return fizzbuzz"