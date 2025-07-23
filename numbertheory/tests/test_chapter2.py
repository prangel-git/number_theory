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


def test_is_euler_brick():
    assert is_euler_brick(44, 117, 240)
    assert is_euler_brick(85, 132, 720)
    assert is_euler_brick(160, 231, 792)
    assert not is_euler_brick(43, 117, 240)
    assert not is_euler_brick(85, 482, 693)
    assert not is_euler_brick(160, 231, 790)


def test_find_sides_from_diagonal():
    assert [(3, 4)] == list(find_sides_from_diagonal(5))


def test_exercise2_14():
    longest_face_diagonal = 267
    for a, b, c in exercise2_14(longest_face_diagonal):
        assert is_euler_brick(a, b, c)
        assert b * b + c * c == longest_face_diagonal * longest_face_diagonal


def test_perimeter_to_number_of_triples():
    number_of_triples = perimeter_to_number_of_triples()
    assert number_of_triples[120] == 3


def test_exercise2_16():
    assert exercise2_16() == 840
