choice = ""

while choice != "3":
    print("1. Say Hello")
    print("2. Tell a Joke")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Hello!")

    elif choice == "2":
        print("Why did the programmer quit his job?")
        print("Because he didn't get arrays.")

print("Goodbye!")