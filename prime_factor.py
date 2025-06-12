# The prime factors of $13195$ are $5, 7, 13$ and $29$.
# What is the largest prime factor of the number $600851475143$?


#what are prime factors -- these are factors of a number that are also prime themsleves
#how do we determine prime factors  a prime number are number that has two factors one and itselves
# so this question wants me to find the largest number that has two factor one and itself that can be divided by 600851475143
num = ""
def highest_prime_factor(n):
    """A function that takes in a number
        and return list it's  prime factors
    """
    i = 2
    factors = []
    while i * i <= n: #continues as long as the i squared is less than the number
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i +=1
           
            
    if n > 1:
        factors.append(n)
    return factors

answer = highest_prime_factor(n=num)
print(f"The rime factors of the number are {answer}")