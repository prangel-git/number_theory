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
    longest_side_diagonal = 3471
    for a, b, c in exercise2_14(longest_side_diagonal):
        d0 = isqrt(a * a + b * b)
        d1 = isqrt(a * a + c * c)
        d2 = isqrt(b * b + c * c)

        print(f"sides {a}, {b}, {c}, diagonals {d0}, {d1}, {d2}")
    # sides 572, 1521, 3120, diagonals 1625, 3172, 3471

    print(list(find_sides_from_diagonal(longest_side_diagonal)))
    # [(204, 3465), (1335, 3204), (1521, 3120), (2295, 2604)]


def main():
    print_2_14()


if __name__ == "__main__":
    main()
