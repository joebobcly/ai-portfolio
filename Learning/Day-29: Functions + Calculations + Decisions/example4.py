def evaluate_funnel(leads, opportunities, customers):

    opportunity_rate = opportunities / leads
    closed_rate = customers / opportunities

    if opportunity_rate >= 0.20 and closed_rate >= 0.25:
        return "Strong"

    elif opportunity_rate >= 0.10 and closed_rate >= 0.15:
        return "Average"

    else:
        return "Weak"

leads = int(input("Enter number of leads: "))
opportunities = int(input("Enter number of opportunities: "))
customers = int(input("Enter number of customers: "))

funnel_rating = evaluate_funnel(leads, opportunities, customers)

print("Funnel rating:", funnel_rating)