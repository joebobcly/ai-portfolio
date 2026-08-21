def describe_number(number):
    if number > 10:
        return "Big"
    elif number == 10:
        return "Exactly ten"
    else:
        return "Small"

result = describe_number(10)

print(result)