from numbertheory.src.utilities import *
from numbertheory.src.chapter2 import *


def main():
    n = 30

    for (u, v), _ in zip(generate_pythagorean_triple_seed(), range(n)):
        a = v * v - u * u
        b = 2 * u * v
        c = v * v + u * u
        print(
            f"u={u}, v={v}. {a}^2 + {b}^2 = {c}^2 is {a*a + b*b == c*c}. Is primitive? {gcd(a,b)}"
        )

    print(exercise2_13())


if __name__ == "__main__":
    main()
