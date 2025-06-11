''' 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
        without any reminder.
        what is the smallest possible number that is evenly divisible by all the number from 1 to 20?
 '''
import math
##break down each number to their prime number
def lcm(a, b):
    """
        A function that takes two numbers and 
        return the least common multiple of a and b
    """
    return a * b // math.gcd(a,b)

result = 1
for num in range(1, 21):
    result = lcm(result, num)


print(f"The smallest number divisible by all numbers from 1-20 si {result}")

