from numbertheory.src.utilities import *

from numbertheory.src.utilities import *
from numbertheory.src.chapter2 import *
from math import isqrt


def main():
    bound = 121
    first_primes = [p for p in primes_up_to(bound)]
    print(first_primes)
    print(len(first_primes))
    print(count_primes(bound))


if __name__ == "__main__":
    main()
