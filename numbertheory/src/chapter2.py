from math import isqrt


def is_square(pyramid_number):
    sqrt_pyramid = isqrt(pyramid_number)
    is_square_number = sqrt_pyramid * sqrt_pyramid == pyramid_number
    return is_square_number


def exercise2_12(bound=1000):
    for a in range(2, bound):
        pyramid_number = a * (a + 1) * (2 * a + 1) // 6
        if is_square(pyramid_number):
            return pyramid_number
    return 0


def exercise2_13(bound=1000):
    return 0
