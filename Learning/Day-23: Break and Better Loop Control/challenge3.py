while True:
    choice = input("Choose: hello, count, skip, or quit: ")

    if choice == "hello":
        print("Hello!")

    elif choice == "count":
        for number in range(1, 6):
            print(number)

    elif choice == "skip":
        continue

    elif choice == "quit":
        break

    else:
        print("Invalid command")

print("Goodbye!")