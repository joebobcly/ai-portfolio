secret = 7

guess = int(input("Guess the number: "))

while guess != secret:
    guess = int(input("Try again: "))

print("You got it!")