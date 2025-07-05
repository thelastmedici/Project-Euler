def sum_of_primes_below(limit):
    sieve = [True] * limit
    sieve[0:2] = [False, False]  # 0 and 1 are not prime

    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            sieve[num * num:limit:num] = [False] * len(range(num * num, limit, num))
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)

# Compute the sum of all primes below 2 million
result = sum_of_primes_below(2_000_000)
print(result)
