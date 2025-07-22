from math import comb

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

    current_value = 5
    crossed_numbers = dict()

    for increment in cycle(increment_value):
        if current_value in crossed_numbers:
            step = crossed_numbers[current_value]
            next = current_value + step
            while  next in crossed_numbers:
                next += step
            crossed_numbers[next] = step
            del crossed_numbers[current_value]
        else:
            crossed_numbers[current_value * current_value] = 6 * current_value
            crossed_numbers[current_value * (current_value + increment)] = 6 * current_value
            yield current_value
        
        current_value += increment

def cycle(numbers):
    while True:
        for num in numbers:
            yield num

def gcd_extended(a, b): 
  
    # Base Case 
    if a == 0 :  
        return b, 0, 1
             
    gcd, x1, y1 = gcd_extended(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
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
    for possible_factors in primes():
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

@lru_cache(maxsize=None,)
def totient(n):
    factors = prime_factorization(n)
    
    t = 1
    for factor, power in factors.items():
        a = factor ** (power - 1)
        t *= (a * factor - a)
    
    return t

def totient_links(n):
    if n == 1:
        return 1
    return totient_links(totient(n))+1

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
        reversed_n = 10 * reversed_n +  last_digit
        n //= 10
    
    return reversed_n

@lru_cache(maxsize=None,)
def fibonnacci(n):
    if n <= 2:
        return 1
    return fibonnacci(n-1)+fibonnacci(n-2)

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
    numerator = den1 +  den0 * num1
    denominator = den0 * den1
    return simplify(numerator, denominator)

def generate_seed():
    i = 2; j = 1
    while True:
        yield i, j
        i = i - 1; j = j + 1
        if i <= j:
            i += j; j = 1

def pythagorean_triples():
    pairs = generate_seed() 
    for u,v in pairs:
        a = u * u - v * v
        b = 2 * u * v
        c = u * u + v * v
        yield a, b, c

