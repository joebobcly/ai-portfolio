def evaluate_campaign(spend, conversions):

    if spend >= 10000 and conversions < 50:
        return "Critical"

    elif spend >= 5000 and conversions < 100:
        return "Review"

    else:
        return "Healthy"

status = evaluate_campaign(7500, 75)

print("Campaign status:", status)