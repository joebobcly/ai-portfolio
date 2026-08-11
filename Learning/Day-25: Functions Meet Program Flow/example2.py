def greet(name):
    print(f"Hello, {name}!")

while True:
    command = input("Enter a command: ")

    if command == "greet":
        user_name = input("What's your name? ")
        greet(user_name)

    elif command == "quit":
        break

    else:
        print("Invalid command")

print("Goodbye!")