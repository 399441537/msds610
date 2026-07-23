from thefuck.core import add, greet


def test_greet_default():
    assert greet() == "Hello, world!"


def test_greet_name():
    assert greet("MSDS610") == "Hello, MSDS610!"


def test_add():
    assert add(2, 3) == 5
