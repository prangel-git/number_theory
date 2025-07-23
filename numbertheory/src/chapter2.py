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
    return 0, 0, 0
