from numbertheory.src.utilities import *


def main():
    p = 7919
    a = 1
    b = 2
    c = 1
    polynomial = lambda x: a * x * x + b * x + c
    discriminant = lambda a, b, c: b * b - 4 * a * c
    answer = 0
    for k in range(p):
        answer += legendre_symbol(polynomial(k), p)
    print(f"the sum is = {answer}")

    d = discriminant(a, b, c)

    print(f"discriminant = {d} is multiple of p? {d % p == 0} ")


if __name__ == "__main__":
    main()
