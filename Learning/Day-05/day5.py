budget = int(input("Campaign budget: "))

if budget >= 50000:
    print("Enterprise campaign")
elif budget >= 10000:
    print("Mid-market campaign")
else:
    print("Small campaign")