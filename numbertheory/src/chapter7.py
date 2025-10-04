from numbertheory.src.utilities import *


def sum_legendre_symbols(p, a, b, c):
    polynomial_quadratic = lambda x: a * x * x + b * x + c
    sumation = 0
    for k in range(p):
        sumation += legendre_symbol(polynomial_quadratic(k), p)
    return sumation


def exercise7_25():
    p = 7919
    a = 2
    b = 42
    c = 21
    polynomial_linear = lambda x: b * x + c
    polynomial_quadratic = lambda x: a * x * x + b * x + c
    discriminant = lambda a, b, c: b * b - 4 * a * c
    answer_a = 0
    answer_b = 0
    answer_c = 0
    for k in range(p):
        answer_a += legendre_symbol(k, p)
        answer_b += legendre_symbol(polynomial_linear(k), p)
        answer_c += legendre_symbol(polynomial_quadratic(k), p)
    print(f"answer_a = {answer_a}")
    print(f"answer_b = {answer_b}")
    print(f"answer_c = {answer_c}")

    d = discriminant(a, b, c)

    print(f"discriminant = {d} is multiple of p? {d % p == 0} ")


def exercise7_25_exploration(p):

    poly_to_sumation = dict()
    for a in range(p):
        for b in range(p):
            for c in range(p):
                sumation = sum_legendre_symbols(p, a, b, c)
                poly_to_sumation[(a, b, c)] = sumation

    return poly_to_sumation
