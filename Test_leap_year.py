import pytest
from Leap_year import isLeapYear


def test_leap_year_divisible_by_4():
    assert isLeapYear(2004) == True
    assert isLeapYear(2020) == True
    assert isLeapYear(2024) == True


def test_leap_year_not_divisible_by_4():
    assert isLeapYear(2001) == False
    assert isLeapYear(2100) == False


def test_leap_year_divisible_by_400():
    assert isLeapYear(1600) == True
    assert isLeapYear(2000) == True
    assert isLeapYear(2400) == True


def test_leap_year_divisible_by_100_but_not_400():
    assert isLeapYear(1700) == False
    assert isLeapYear(1800) == False
    assert isLeapYear(1900) == False
    assert isLeapYear(2100) == False


def test_leap_year_negative_year():
    assert isLeapYear(-2004) == True


def test_leap_year_zero_year():
    assert isLeapYear(0) == True


if __name__ == "__main__":
    pytest.main()