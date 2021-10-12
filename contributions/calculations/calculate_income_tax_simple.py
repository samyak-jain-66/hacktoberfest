def calculate_income_tax(income, relationship_status):
    single = relationship_status == 0  # True or False
    high_income = income > 4000  # True or False
    if high_income and single:
        tax = 0.26
    elif not high_income and not single:
        tax = 0.18
    else:
        tax = 0.22
    return income * tax


income = int(input("What's your income? "))
relationship_status = int(
    input("What's your relationship status?\n0: Single\n1: Married\n")
)
tax = calculate_income_tax(income, relationship_status)
print(f"Your tax is {tax} €.")
