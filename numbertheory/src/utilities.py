from math import comb, isqrt

from functools import lru_cache


def euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = euclidean_algorithm(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        if gcd > 0:
            return gcd, x, y
        return -gcd, -x, -y


def primes():
    yield 2
    yield 3

    increment_value = [2, 4]

    crossed_numbers = dict()

    current_value = 5
    for increment in cycle(increment_value):
        if current_value in crossed_numbers:
            _update_crossed_numbers(current_value, crossed_numbers)
        else:
            _cross_next_multiples(current_value, increment, crossed_numbers)
            yield current_value

        current_value += increment


def primes_up_to(bound):
    sqrt_bound = isqrt(bound)

    yield 2
    yield 3

    increment_value = [2, 4]

    crossed_numbers = dict()

    current_value = 5
    for increment in cycle(increment_value):
        if current_value > bound:
            break
        if current_value in crossed_numbers:
            _update_crossed_numbers(current_value, crossed_numbers)
        else:
            if current_value <= sqrt_bound:
                _cross_next_multiples(current_value, increment, crossed_numbers)
            yield current_value

        current_value += increment


def _update_crossed_numbers(number_to_update, crossed_numbers_dict):
    step = crossed_numbers_dict[number_to_update]
    next = number_to_update + step
    while next in crossed_numbers_dict:
        next += step
    crossed_numbers_dict[next] = step
    del crossed_numbers_dict[number_to_update]


def _cross_next_multiples(current_value, increment, crossed_numbers):
    crossed_numbers[current_value * current_value] = 6 * current_value
    crossed_numbers[current_value * (current_value + increment)] = 6 * current_value


def cycle(numbers):
    while True:
        for num in numbers:
            yield num


def sequence_from_cycle(initial_value, numbers):
    current_value = initial_value
    while True:
        for num in numbers:
            yield current_value
            current_value += num


def gcd_extended(a, b):

    # Base Case
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcd_extended(b % a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def gcd(a, b):
    g, _, _ = gcd_extended(a, b)
    return g


def primorial(n):
    prime_generator = primes()
    pr = 1
    for _ in range(n):
        pr *= next(prime_generator)

    return pr


def relative_primes(n):
    return [m for m in range(1, n) if gcd(n, m) == 1]


def order_of(m, n):

    if gcd(m, n) != 1:
        return 0

    order = 1
    current = m % n
    while current != 1:
        order += 1
        current *= m
        current %= n

    return order


def prime_factorization(n):
    factors = dict()
    if n <= 1:
        return factors
    for possible_factors in primes_up_to(n):
        while n % possible_factors == 0:
            factors[possible_factors] = factors.get(possible_factors, 0) + 1
            n //= possible_factors
        if n == 1:
            break

    return factors


def factorize(n):
    factors = dict()
    if n <= 1:
        return factors
    for possible_factors in range(2, n + 1):
        while n % possible_factors == 0:
            factors[possible_factors] = factors.get(possible_factors, 0) + 1
            n //= possible_factors
        if n == 1:
            break

    return factors


def divisors(n):
    if n == 0:
        return []
    divs = set()
    d = 1
    while d * d <= n:
        if n % d == 0:
            divs.add(d)
            divs.add(abs(n) // d)
        d += 1
    return sorted(divs)


@lru_cache(
    maxsize=None,
)
def totient(n):
    factors = prime_factorization(n)

    t = 1
    for factor, power in factors.items():
        a = factor ** (power - 1)
        t *= a * factor - a

    return t


def totient_links(n):
    if n == 1:
        return 1
    return totient_links(totient(n)) + 1


def inverse_totient(phi_n):
    # https://math.stackexchange.com/questions/265397/inversion-of-the-euler-totient-function
    lower_bound = phi_n
    upper_bound = 2 * (3 ** totient_links(phi_n))
    inverses = []
    for n in range(lower_bound, upper_bound + 1):
        if totient(n) == phi_n:
            inverses.append(n)
    return inverses


def reverse(n):
    reversed_n = 0

    while n != 0:
        last_digit = n % 10
        reversed_n = 10 * reversed_n + last_digit
        n //= 10

    return reversed_n


@lru_cache(
    maxsize=None,
)
def fibonnacci(n):
    if n <= 2:
        return 1
    return fibonnacci(n - 1) + fibonnacci(n - 2)


def multinomial(lst):
    prod = 1
    acc = 0
    for k in range(len(lst)):
        acc += lst[k]
        prod *= comb(acc, lst[k])
    return prod


def egyptian_fraction(numerator, denominator):
    numerator, denominator = simplify(numerator, denominator)

    if numerator == 1:
        return [denominator]

    greedy_denominator = (denominator // numerator) + 1
    next_numerator = numerator * greedy_denominator - denominator
    next_denominator = denominator * greedy_denominator

    return [greedy_denominator] + egyptian_fraction(next_numerator, next_denominator)


def simplify(numerator, denominator):
    g = gcd(numerator, denominator)
    numerator //= g
    denominator //= g
    return numerator, denominator


def egyptian_to_numerator_denominator(egyptian_representation):
    if not egyptian_representation:
        return 0, 1

    den0 = egyptian_representation[0]
    num1, den1 = egyptian_to_numerator_denominator(egyptian_representation[1:])
    numerator = den1 + den0 * num1
    denominator = den0 * den1
    return simplify(numerator, denominator)


def pythagorean_seed():
    u = 1
    v = 2
    while True:
        if gcd(v, u) == 1:
            yield u, v
        u = u + 1
        v = v - 1

        if u >= v:
            v = v + u + 1
            u = 1


def pythagorean_seed_and_triple():
    pairs = pythagorean_seed()
    for u, v in pairs:
        a = v * v - u * u
        b = 2 * u * v
        c = u * u + v * v
        yield (u, v), (a, b, c)


def pythagorean_triples():
    for _, triple in pythagorean_seed_and_triple():
        yield triple


def is_prime(n):
    if n < 0:
        return is_prime(-n)
    elif n == 0 or n == 1:
        return False
    elif n == 2 or n == 3:
        return True

    max_factor = isqrt(n)

    for possible_factor in primes_up_to(max_factor):
        if n % possible_factor == 0:
            return False

    return True


# TODO: Improve performance. First by generating only primes up to sqrt(n). Then by Legendre formula
def count_primes(n):
    count = 0
    for p in primes_up_to(n):
        count += 1

    return count


def padic_valuation(p, n):
    count = 0
    while n % p == 0:
        count += 1
        n //= p
    return count


def primitive_roots(n):
    totient_p = totient(n)
    factors = factorize(totient_p)

    for candidate in range(2, n):
        if _is_primitive_root(n, totient_p, factors, candidate):
            yield candidate


def _is_primitive_root(n, totient_p, factors, candidate):

    is_primitive = True
    for factor in factors:
        if pow(candidate, totient_p // factor, n) == 1:
            is_primitive = False
            break
    return is_primitive


def legendre_symbol(a, p):
    """
    if a == 1:
        return 1
    if a == -1:
        if p % 4 == 1:
            return 1
        else:
            return -1
    if a == 2:
        if p % 8 == 1 or p % 8 == 7:
            return 1
        else:
            return -1
    """
    if a % p == 0:
        return 0

    return 2 * (pow(a, (p - 1) // 2, p) == 1) - 1
