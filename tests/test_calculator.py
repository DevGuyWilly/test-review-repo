"""Tests for the calculator module."""

from app.calculator import add, subtract, multiply, divide
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(15, 3) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
