pizza = [
    ("Hawaiian", "Small", 180),
    ("Hawaiian", "Medium", 200),
    ("Hawaiian", "Large", 500),
    ("Pepperoni", "Small", 180),
    ("Pepperoni", "Medium", 260),
    ("Pepperoni", "Large", 600)
]

select = input("Select pizza: ").title()

for item in pizza:
    if item[0] == select:
        print(item[0], item[1], item[2])