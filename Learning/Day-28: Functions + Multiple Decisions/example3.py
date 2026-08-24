def evaluate_campaign(spend, conversions):

    if spend >= 10000 and conversions < 50:
        return "Critical"

    elif spend >= 5000 and conversions < 100:
        return "Review"

    else:
        return "Healthy"

spend = int(input("Enter campaign spend: "))
conversions = int(input("Enter conversions: "))

status = evaluate_campaign(spend, conversions)

print("Campaign status:", status)