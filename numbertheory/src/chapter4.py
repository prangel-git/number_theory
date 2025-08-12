def exercise_4_47():
    polynomial = lambda x: (x**2 - 2 * x - 4) % 11
    print(f"Polynomial({52})={polynomial(52)}")
    print(f"Polynomial({82})={polynomial(82)}")
    print(f"Polynomial({107})={polynomial(107)}")

    print(f"52 == {52 % 11}")
    print(f"82 == {82 % 11}")
    print(f"107 == {107 % 11}")

    polynomial = lambda x: (x**2 - 2) % 3
    print(f"f(x) = x**2-2 mod 3, f({0}) {polynomial(0)}")
    print(f"f(x) = x**2-2 mod 3, f({1}) {polynomial(1)}")
    print(f"f(x) = x**2-2 mod 3, f({2}) {polynomial(2)}")

    polynomial = lambda x: 3 * x * (x - 3) % 21
    pol_values = [polynomial(x) for x in range(21)]
    print(pol_values)


def exercise_4_58():
    eliptic = lambda x, y: (y**2 - x**3 + 8 * x) % 101
    solutions = []
    for x in range(101):
        for y in range(101):
            if eliptic(x, y) == 0:
                solutions.append((x, y))

    print(solutions)
