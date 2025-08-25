from math import isqrt

# Exercise 5.26 Out of the first million natural numbers, how many satisfy the conditions of Theorem 5.7.1 and can hence be written as a sum of two squares?

# Theorem 5.7.1: An integer n can be written as a sum of two integer squares if and only if v_p(n) is even for every prime p ≡ 3 mod 4.


def exercise_5_26(bound=1_000_000):
    answer = dict()

    sqrt_bound = isqrt(bound)
    for k in range(sqrt_bound + 1):
        for l in range(k + 1, sqrt_bound + 1):
            sum_of_squares = (k * k) + (l * l)
            if sum_of_squares <= bound:
                answer[sum_of_squares] = answer.get(sum_of_squares, 0) + 1
            else:
                break

    return answer
