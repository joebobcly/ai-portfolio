def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

age = int(input("What is your age?: "))

result = check_age(age)

print(result)