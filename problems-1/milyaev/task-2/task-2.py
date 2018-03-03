import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    if n < 2:
        return False
    max_factor = int(math.sqrt(n))
    return all(n % i for i in range(3, max_factor + 1, 2))


print(is_prime(-2))
