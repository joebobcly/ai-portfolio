age = 16
has_parent = True
has_ticket = False

if (age >= 18 or has_parent) and not has_ticket:
    print("Cannot enter yet.")
else:
    print("Enjoy the show!")