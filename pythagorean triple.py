# Loop through possible values of a
for a in range(1, 1000):
    # Loop through values of b greater than a
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b  # Since a + b + c = 1000
        if a * a + b * b == c * c:  # Check Pythagorean condition
            print(f"The triplet is: a = {a}, b = {b}, c = {c}")
            print(f"The product abc is: {a * b * c}")
            break
    else:
        continue
    break
