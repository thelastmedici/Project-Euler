#what is the  10 001st prime 
import math

def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    # Only check odd divisors up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_nth_prime(nth):
    """Return the nth prime number."""
    count = 0
    num = 1
    while count < nth:
        num += 1
        if is_prime(num):
            count += 1
    return num

nth_prime = find_nth_prime(10001)
print(f" {nth_prime}")
