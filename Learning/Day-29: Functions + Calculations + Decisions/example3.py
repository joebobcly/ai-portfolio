def evaluate_campaign(spend, revenue, conversions):

    roi = revenue / spend
    cost_per_conversion = spend / conversions

    if roi >= 4 and cost_per_conversion <= 150:
        return "Excellent"

    elif roi >= 2 and cost_per_conversion <= 250:
        return "Good"

    else:
        return "Poor"

spend = int(input("Enter campaign spend: "))
revenue = int(input("Enter campaign revenue: "))
conversions = int(input("Enter conversions: "))

rating = evaluate_campaign(spend, revenue, conversions)

print("Campaign rating:", rating)