def count_up():
    for number in range(1, 4):
        print(number)

def count_down():
    for number in range(3, 0, -1):
        print(number)

while True:
    command = input("Enter a command: ")

    if command == "up":
        count_up()

    elif command == "down":
        count_down()

    elif command == "quit":
        break

    else:
        print("Invalid command")

print("Finished!")