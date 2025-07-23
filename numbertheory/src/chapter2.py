from numbertheory.src.utilities import *
from math import isqrt


def is_square(number):
    sqrt_number = isqrt(number)
    is_square_number = sqrt_number * sqrt_number == number
    return is_square_number


def is_tetahedral(number):
    index = 1
    possible_number = index * (index + 1) * (index + 2) // 6
    while possible_number <= number:
        if possible_number == number:
            return True
        index += 1
        possible_number = index * (index + 1) * (index + 2) // 6
    return False


def exercise2_12(bound=1000):
    for a in range(2, bound):
        pyramid_number = a * (a + 1) * (2 * a + 1) // 6
        if is_square(pyramid_number):
            return pyramid_number
    return 0


def exercise2_13(bound=1000):
    for a in range(5, bound):
        tetahedral = a * (a + 1) * (a + 2) // 6
        if is_square(tetahedral):
            return tetahedral
    return 0


def is_euler_brick(a, b, c):
    if not is_square(a * a + b * b):
        return False
    if not is_square(a * a + c * c):
        return False
    if not is_square(b * b + c * c):
        return False

    return True


def exercise2_14(bound=3471):
    a0, b0, c0 = (0, 0, 0)
    diagonal0 = 0
    for a in range(1, bound):
        for b in range(a + 1, bound):
            if is_square(a * a + b * b):
                for c in range(b + 1, bound):
                    diagonal = isqrt(b * b + c * c)
                    if diagonal > bound:
                        break
                    if is_euler_brick(a, b, c) and diagonal > diagonal0:
                        a0, b0, c0 = (a, b, c)

    return a0, b0, c0


def perimeter_to_number_of_triples(bound=1000):
    number_of_triples = dict()

    for seed, triple in pythagorean_seed_and_triple():
        (u, v) = seed
        (a, b, c) = triple
        perimeter = a + b + c

        if perimeter > bound and u == 1:
            break

        for p in range(perimeter, bound + 1, perimeter):
            number_of_triples[p] = number_of_triples.get(p, 0) + 1

    return number_of_triples


def exercise2_16(bound=1000):
    perimeter_triples = perimeter_to_number_of_triples()
    return max(perimeter_triples, key=lambda k: perimeter_triples[k])
