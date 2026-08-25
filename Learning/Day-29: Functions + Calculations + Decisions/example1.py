def evaluate_performance(spend, revenue):

    roi = revenue / spend

    if roi >= 3:
        return "Strong"

    elif roi >= 2:
        return "Average"

    else:
        return "Weak"