def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 1:
        return False
    sum_factors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_factors += i
            if i != n // i:
                sum_factors += n // i
    return sum_factors == n
