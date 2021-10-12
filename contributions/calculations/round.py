def round_two_decimals(number):
    result = round(number * 100) / 100
    print(result)


def round__to_next_whole_number(number):
    # truncates the number and adds 1
    result = int(number) + 1
    print(result)


def round_to_previous_whole_number(number):
    # truncates the number
    result = int(number)
    print(result)


round_two_decimals(18 / 7)
round__to_next_whole_number(18 / 7)
round_to_previous_whole_number(18 / 7)
