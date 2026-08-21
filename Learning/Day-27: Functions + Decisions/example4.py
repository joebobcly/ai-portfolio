def calculate_discount(price, member):
    if member == "yes":
        return(price * .8)
    else:
        return(price)

price = float(input("Enter the price: "))
member = input("Are you a member?: ")

final_price = calculate_discount(price, member)

print("Final price: ", final_price)