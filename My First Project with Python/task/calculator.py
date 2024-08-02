from collections import OrderedDict

print("Earned amount:")

# Declaring an OrderedDict in a single statement
# by passing a list of tuples to its constructor.
earnings = OrderedDict([
    ("Bubblegum", 202),
    ("Toffee", 118),
    ("Ice cream", 2250),
    ("Milk chocolate", 1680),
    ("Doughnut", 1075),
    ("Pancake", 80)
])

for item, amount in earnings.items():
    print(f"{item}: ${amount}")

income = sum(earnings.values())

print(f"\nIncome: ${income}")

print("Staff expenses:")
staff_exp = int(input())

print("Other expenses:")
other_exp = int(input())

net_income = income - staff_exp - other_exp
print(f"Net income: ${net_income}")