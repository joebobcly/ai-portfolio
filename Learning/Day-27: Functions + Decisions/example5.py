def calculate_shipping(total, member):
    if member == "yes" and total >= 50:
        return 0
    elif member == "yes" and total < 50:
        return 5
    else:
        return 10

total = float(input("Enter order total: "))
member = input("Are you a member?: ")

shipping_cost = calculate_shipping(total, member)

print("Shipping cost: ", shipping_cost)