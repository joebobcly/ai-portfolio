def count_by(limit, step):
    for number in range(step, limit + 1, step):
        print(number)

limit = int(input("What number should I count to? "))
step = int(input("What should I count by? "))

count_by(limit, step)