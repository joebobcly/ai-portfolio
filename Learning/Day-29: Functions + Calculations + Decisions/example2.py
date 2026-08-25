def evaluate_campaign(spend, revenue, conversions):

    roi = revenue / spend
    cost_per_conversion = spend / conversions

    if roi >= 4 and cost_per_conversion <= 100:
        return "Excellent"

    elif roi >= 2 and cost_per_conversion <= 200:
        return "Good"

    else:
        return "Poor"