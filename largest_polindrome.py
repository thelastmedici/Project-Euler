#Find the largest palindrome made from the product of two 
# #3-digit numbers.
# def check_polindrome(n):
#     """
#     A function that check if a number can be rearraged from left ->right
#     and right -> left and would still be same
#   """

#STEP 1: what is a polindrome
#### Answer: a polindronme is a number that when rearraged both forward and backwards are the same

#Step 2:Defining the search space: i.e peoduct of three digit num i.e from 100 to 999
##### in this search space we exclude duplicated i.e 123 * 456 = 456 * 123
def find_largest_palindrome_product():
    largest_palindrome = 0
    def palindrome_checker(word):
        """A function that takes a word 
        reverses it and check if it is a 
        palindrome
        """
        reversed_string = ""
        for i in range(len(word)-1, -1, -1): #starts. stop, step
            reversed_string+=word[i]

        if word == reversed_string:
            return True
        else:
            return False

    product = ""
    for a in range(100, 1000): #first number between 100 -> 999
        for b in range(100, 1000): #second number between 100 -> 999
            product = a * b
            product = str(product)
            if palindrome_checker(word=product):
                if int(product) > int(largest_palindrome):
                    largest_palindrome = int(product)
    
    return largest_palindrome

result = find_largest_palindrome_product()
print(f"The largest palindrome is:{result} ")

