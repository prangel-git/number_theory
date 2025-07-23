from numbertheory.src.chapter2 import *


def test_is_square():
    assert is_square(2) == False
    assert is_square(9) == True


def test_exercise2_12():
    assert exercise2_12() == 4900
