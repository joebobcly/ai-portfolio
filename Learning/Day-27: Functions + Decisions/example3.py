def check_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 60:
        return "Passed"
    else:
        return "Failed"

score = int(input("Enter your score: "))

result = check_score(score)

print(result)