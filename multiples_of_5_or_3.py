"""
if we list all the natural numbers below 10 that are multiples of 
3 or 5, we get 3,5,6 and 9. the sum  of these multiples is 23.
find the sum of all the multiples of 3 or 5 below 1000
"""
list_of_multiples =[]
for n in range(0, 1001):
        if n < 1000:
            if n % 3 == 0 or n % 5 == 0: 
                list_of_multiples.append(n)
print(sum(list_of_multiples))
            