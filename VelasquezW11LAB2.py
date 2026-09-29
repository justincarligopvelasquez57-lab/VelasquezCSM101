pizza_flavors = ("hawaiian", "pepperoni", "vanilla", "cheese")


pizza_sizes = ["small", "medium", "large"]
pizza_prices = [180, 250, 300]

while True:

    velasquez_flavor = input("Enter pizza flavor (hawaiian/pepperoni/vanilla/cheese): ").lower()

    if velasquez_flavor in pizza_flavors:
        print("You selected", velasquez_flavor.title(), "Pizza.")
        print()
    else:
        print("Invalid pizza flavor.")
        print()
        continue

    velasquez_size = input("Enter size (Small/Medium/Large): ").lower()

    if velasquez_size in pizza_sizes:
        index = pizza_sizes.index(velasquez_size)
        velasquez_price = pizza_prices[index]
        print("\nPizza price:", velasquez_price)
    else:
        print("Invalid size.")
        print()

    again = input("\nDo you want to enter again? (Y/N): ")

    if again.upper() != "Y":
        print("Program ended.")
        break