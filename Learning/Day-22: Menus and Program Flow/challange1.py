choice = ""

while choice != "3":
    print("1. Say Hi")
    print("2. Say Bye")
    print("3. Quit")
    
    choice = input("Choose an option:")

    if choice == "1":
        print("Hi!")

    elif choice == "2":
        print("Bye!")

    elif choice == "3":
        pass

    else:
        print("Invalid choice")

print("Program ended.")