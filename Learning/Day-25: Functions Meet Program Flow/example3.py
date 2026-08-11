def count_to_five():
    for number in range(1, 6):
        print(number)

while True:
    command = input("Enter a command: ")

    if command == "hello":
        print("Hello there!")

    elif command == "count":
        count_to_five()

    elif command == "quit":
        break

    else:
        print("Invalid command")

print("Goodbye!")