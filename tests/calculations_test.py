from src.calculations import get_nth_fibonacci


def test_get_nth_fibonacci_zero():
    assert get_nth_fibonacci(0) == 0


def test_get_nth_fibonacci_one():
    assert get_nth_fibonacci(1) == 1


def test_get_nth_fibonacci_ten():
    assert get_nth_fibonacci(10) == 55