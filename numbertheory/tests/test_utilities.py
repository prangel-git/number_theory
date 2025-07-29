import pytest
from numbertheory.src.utilities import *


@pytest.mark.parametrize(
    "a, b, expected_gcd",
    [
        (30, 20, 10),
        (17, 13, 1),
        (0, 5, 5),
        (5, 0, 5),
        (0, 0, 0),
        (100, 25, 25),
        (270, 192, 6),
        (-25, 15, 5),
        (25, -15, 5),
        (-25, -15, 5),
        (123456, 7890, 6),
        (35, 64, 1),
    ],
)
def test_euclidean_algorithm_gcd_and_bezout(a, b, expected_gcd):
    gcd, x, y = euclidean_algorithm(a, b)
    assert gcd == expected_gcd
    assert a * x + b * y == gcd


def test_euclidean_algorithm_commutativity():
    a, b = 56, 15
    gcd1, x1, y1 = euclidean_algorithm(a, b)
    gcd2, x2, y2 = euclidean_algorithm(b, a)
    assert gcd1 == gcd2
    assert a * x1 + b * y1 == gcd1
    assert b * x2 + a * y2 == gcd2


def test_euclidean_algorithm_large_numbers():
    a, b = 123456789, 987654321
    gcd, x, y = euclidean_algorithm(a, b)
    assert gcd == 9
    assert a * x + b * y == gcd


def test_prime_generator():
    primes_smaller_than_100 = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
    ]
    generated_primes = []
    for prime in primes():
        if prime < 100:
            generated_primes.append(prime)
        else:
            break

    assert generated_primes == primes_smaller_than_100


def test_cycles_generator():
    numbers = [1, 2, 1]
    expected_cycle = [1, 2, 1, 1, 2, 1]
    generated_cycle = []
    for num in cycle(numbers):
        if len(generated_cycle) < 6:
            generated_cycle.append(num)
        else:
            break
    assert generated_cycle == expected_cycle


def test_gcd():
    a = 15
    b = 35
    g, x, y = gcd_extended(a, b)

    expected_gcd = 5
    expected_x = -2
    expected_y = 1

    assert expected_gcd == g
    assert expected_x == x
    assert expected_y == y


@pytest.mark.parametrize(
    "input, expected_answer", [(1, 2), (2, 6), (3, 30), (4, 210), (5, 2310)]
)
def test_primorial(input, expected_answer):
    answer = primorial(input)
    assert answer == expected_answer


@pytest.mark.parametrize(
    "input, expected_answer", [(6, [1, 5]), (30, [1, 7, 11, 13, 17, 19, 23, 29])]
)
def test_relative_primes(input, expected_answer):
    answer = relative_primes(input)
    assert answer == expected_answer


@pytest.mark.parametrize(
    "input, expected_answer", [(6, {2: 1, 3: 1}), (30, {2: 1, 3: 1, 5: 1}), (8, {2: 3})]
)
def test_prime_factorization(input, expected_answer):
    answer = prime_factorization(input)
    assert answer == expected_answer


@pytest.mark.parametrize("input, expected_answer", [(3, 2), (7, 6), (10, 4)])
def test_totient(input, expected_answer):
    answer = totient(input)
    assert answer == expected_answer


def test_reverse():
    assert 1235 == reverse(5321)


def test_totient_links():
    assert 5 == totient_links(24)


def test_inverse_totient():
    assert inverse_totient(24) == [35, 39, 45, 52, 56, 70, 72, 78, 84, 90]
    assert inverse_totient(120) == [
        143,
        155,
        175,
        183,
        225,
        231,
        244,
        248,
        286,
        308,
        310,
        350,
        366,
        372,
        396,
        450,
        462,
    ]


def test_fibonacci():
    fibonacci_numbers = [fibonnacci(k) for k in range(1, 11)]
    assert [1, 1, 2, 3, 5, 8, 13, 21, 34, 55] == fibonacci_numbers


def test_divisors():
    f = divisors(75)
    assert f == [1, 3, 5, 15, 25, 75]


def test_divisors_of_a_square():
    f = divisors(25)
    assert f == [1, 5, 25]


def test_multinomial():
    assert multinomial([3, 2]) == 10
    assert multinomial([3, 2, 2]) == 210


def test_egyptian_fraction_one_over_six():
    assert egyptian_fraction(1, 6) == [6]


def test_egyptian_fraction():
    assert egyptian_fraction(5, 6) == [2, 3]


def test_egyptian_to_numerator_denominator():
    assert egyptian_to_numerator_denominator([2, 3]) == (5, 6)


def test_pythagorean_triples():
    pythagorean_iterator = pythagorean_triples()
    for _ in range(50):
        a, b, c = next(pythagorean_iterator)
        assert a * a + b * b == c * c


def test_generate_natural_numbers_pairs():
    pairs = pythagorean_seed()
    assert (1, 2) == next(pairs)
    assert (1, 4) == next(pairs)
    assert (2, 3) == next(pairs)
    assert (1, 6) == next(pairs)
    assert (2, 5) == next(pairs)


def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(31) == True
    assert is_prime(31 * 31) == False
    assert is_prime(27644437) == True
    assert is_prime(27644437 * 877) == False
