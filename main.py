from numbertheory.src.utilities import *
from numbertheory.src.chapter7 import *


def main():
    p = 19
    poly_to_sum = exercise7_25_exploration(p)
    # discriminant = lambda a, b, c: b * b - 4 * a * c

    possible_values = set()

    for value in poly_to_sum.values():
        possible_values.add(value)

    print(possible_values)

    """
    for key, value in poly_to_sum.items():
        a, b, c = key
        delta = discriminant(a, b, c)
        print(f"{a} x**2 + {b} x + {c}: discriminant = {delta}, sum =  {value}")
    """


if __name__ == "__main__":
    main()
