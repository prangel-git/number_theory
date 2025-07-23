from numbertheory.src.utilities import *
from numbertheory.src.chapter2 import *
from math import isqrt


def testing_pythagorean_tripes():
    n = 30

    for (u, v), _ in zip(pythagorean_seed(), range(n)):
        a = v * v - u * u
        b = 2 * u * v
        c = v * v + u * u
        print(
            f"u={u}, v={v}. {a}^2 + {b}^2 = {c}^2 is {a*a + b*b == c*c}. Is primitive? {gcd(a,b)}"
        )


def print_2_13():
    print(exercise2_13())


def print_2_14():
    bound = 3471
    a, b, c = exercise2_14(bound)
    d0 = isqrt(a * a + b * b)
    d1 = isqrt(a * a + c * c)
    d2 = isqrt(b * b + c * c)

    print(f"sides {a}, {b}, {c}, diagonals {d0}, {d1}, {d2}")
    # sides 2160, 2268, 2475, diagonals 3132, 3285, 3357


def main():
    testing_pythagorean_tripes()


if __name__ == "__main__":
    main()
