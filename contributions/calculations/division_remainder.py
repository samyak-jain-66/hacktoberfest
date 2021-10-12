def calculate_remainder(x, y):
    if y == 0:
        print("Division by zero!")
    else:
        result = x % y
        print("The remainder is", result)


calculate_remainder(25, 12)
