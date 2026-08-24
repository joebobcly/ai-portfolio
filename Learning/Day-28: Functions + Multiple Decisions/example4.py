def evaluate_campaign(spend, conversions, days_running):

    if spend >= 10000 and conversions < 50 and days_running >= 7:
        return "Critical"

    elif spend >= 5000 and conversions < 100 and days_running >= 5:
        return "Review"

    else:
        return "Healthy"

spend = int(input("Enter campaign spend: "))
conversions = int(input("Enter conversions: "))
days_running = int(input("Enter days running: "))

status = evaluate_campaign(spend, conversions, days_running)

print("Campaign status:", status)