from seasons import convert_input, minutes_calculator
from datetime import date


def test_seasons():
    assert convert_input("1999-01-01") == date(1999, 1, 1)
    assert minutes_calculator(date(1999, 1, 1)) == (
        date.today() - date(1999, 1, 1)).total_seconds() / 60
    assert convert_input("February 6th, 1998") == None
