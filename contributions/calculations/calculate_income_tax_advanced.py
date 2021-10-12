import enum


class RelationShipStatus(enum.Enum):
    single = 0
    married = 1


class Person:
    def __init__(self, income, relationship_status):
        self.income = income
        self.relationship_status = relationship_status


def calculate_income_tax(person):
    single = person.relationship_status == RelationShipStatus.single
    high_income = person.income > 4000
    if high_income and single:
        tax = 0.26
    elif not high_income and not single:
        tax = 0.18
    else:
        tax = 0.22
    return person.income * tax


income = input("What's your income? ")
relationship_status = input("What's your relationship status?\n0: Single\n1: Married\n")
person = Person(int(income), RelationShipStatus(int(relationship_status)))
tax = calculate_income_tax(person)
print(f"Your tax is {tax} €.")
