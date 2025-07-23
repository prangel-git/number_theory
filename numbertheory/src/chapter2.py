from math import isqrt


def exercise2_12(bound=1000):
    for a in range(2, bound):
        pyramid_number = a * (a + 1) * (2 * a + 1) // 6
        sqrt_pyramid = isqrt(pyramid_number)
        is_square_number = sqrt_pyramid * sqrt_pyramid == pyramid_number
        if is_square_number:
            return pyramid_number
    return 0
