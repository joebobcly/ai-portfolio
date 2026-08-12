def add(number1, number2):
    return number1 + number2

def multiply(number1, number2):
    return number1 * number2

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

sum_result = add(number1, number2)
product_result = multiply(number1, number2)

print("Sum:", sum_result)
print("Product:", product_result)