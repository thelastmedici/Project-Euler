def calculate_difference(limit):
    """
    Calculate the difference between the square of the sum and the sum of the squares 
    of the first 'limit' natural numbers.
    
    Parameters:
        limit (int): The upper bound of the natural numbers (inclusive).
    
    Returns:
        tuple: A tuple containing (sum_of_squares, square_of_sum, difference)
    """
    
    sum_of_squares_list = []
    sum_numbers = 0
    
    for n in range(0, limit + 1):
        sum_numbers += n                      # accumulate the sum of numbers
        sum_of_squares_list.append(n * n)       # accumulate the square of each number
    
    sum_of_squares = sum(sum_of_squares_list)       # sum of the squares
    square_of_sum = sum_numbers ** 2                # square of the sum
    difference = square_of_sum - sum_of_squares     # calculate the difference
    
    return sum_of_squares, square_of_sum, difference

 
##if limit is 100
if __name__ == "__main__":
    limit = 100
    sum_squares, square_of_sum, diff = calculate_difference(limit=limit)
    print(f"The sum of the suares is {sum_squares}")
    print(f"The square of the sum is {square_of_sum}")
    print(f"The differnce is {diff}")
