while True:
    command = input("Enter a command: ")

    if command == "hello":
        print("Hello there!")

    elif command == "count":
        for number in range(1, 6):
            print(number)

    elif command == "quit":
        break

    else:
        print("Invalid command")

print("Goodbye!")