from plates import is_valid


def test_plates():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("50CS") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("12345") == False