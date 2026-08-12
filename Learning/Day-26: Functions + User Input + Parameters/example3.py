def count_down(start):
    for number in range(start, 0, -1):
        print(number)

start_number = int(input("Where should I start? "))

count_down(start_number)