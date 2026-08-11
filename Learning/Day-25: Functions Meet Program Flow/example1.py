def count():
    for number in range(1, 4):
        print(number)

while True:
    command = input("Enter a command: ")

    if command == "count":
        count()

    elif command == "quit":
        break

    else:
        print("Invalid command")

print("Goodbye!")