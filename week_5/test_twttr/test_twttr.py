from twttr import shorten


def test_twttr():
    assert shorten("Is today May 16, 2022?") == "s tdy My 16, 2022?"