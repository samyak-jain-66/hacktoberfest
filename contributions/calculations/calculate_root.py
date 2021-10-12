def calculate_root(number, root):
    # an nth root can be written as ^ (1 / n):
    result = number ** (1 / root)
    print(result)


calculate_root(288, 3)
