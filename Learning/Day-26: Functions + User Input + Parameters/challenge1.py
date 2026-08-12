def add(number1, number2):
    return number1 + number2

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

total = add(number1, number2)

if total > 20:
    print("That's a big number!")

else:
    print("That's a small number!")