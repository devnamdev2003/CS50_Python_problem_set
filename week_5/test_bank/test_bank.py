from bank import value


def test_bank():
    assert value("Hello") == 0
    assert value("Hi") == 20
    assert value("Ciao") == 100