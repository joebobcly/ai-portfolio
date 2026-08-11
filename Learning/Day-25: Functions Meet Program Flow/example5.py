def count_up():
    for number in range(1, 6):
        print(number)

def count_down():
    for number in range(5, 0, -1):
        print(number)

def even_numbers():
    for number in range(2, 11, 2):
        print(number)

while True:
    command = input("Enter a command: ")

    if command == "up":
        count_up()

    elif command == "down":
        count_down()

    elif command == "even":
        even_numbers()

    elif command == "quit":
        break

    else:
        print("Invalid command")

print("Goodbye!")