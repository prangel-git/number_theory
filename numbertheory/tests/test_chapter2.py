from numbertheory.src.chapter2 import *


def test_is_square():
    assert is_square(2) == False
    assert is_square(9) == True


def test_is_tetahedral():
    assert is_tetahedral(35) == True
    assert is_tetahedral(56) == True
    assert is_tetahedral(220) == True
    assert is_tetahedral(24) == False
    assert is_tetahedral(32) == False
    assert is_tetahedral(42) == False


def test_exercise2_12():
    assert exercise2_12() == 4900


def test_exercise2_13():
    square_tetahedral = exercise2_13()
    assert is_square(square_tetahedral)
    assert is_tetahedral(square_tetahedral)


def test_exercise2_13_answer():
    assert 19600 == exercise2_13()
