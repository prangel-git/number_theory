from numbertheory.src.utilities import gcd


def fermat_number(n):
    return (2 ** (2**n)) + 1


def exercise_3_39():
    bound = 21
    f = [fermat_number(n) for n in range(bound)]
    for f_n in f[:10]:
        print(f"f_n = {f_n}")

    for i in range(bound - 1):
        for j in range(i + 1, bound):
            g = gcd(f[i], f[j])
            print(f"gcd(f_{i}, f_{j}) = {g}")
