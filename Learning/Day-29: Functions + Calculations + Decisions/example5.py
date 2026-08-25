def calculate_conversions(opportunities, customers):
    conversion_rate = customers / opportunities
    return conversion_rate

def evaluate_conversions(conversion_rate):

    if conversion_rate >= 0.30:
        return "Excellent"

    elif conversion_rate >= 0.20:
        return "Good"

    else:
        return "Needs Improvement"

opportunities = int(input("Enter number of opportunities: "))
customers = int(input("Enter number of customers: "))

conversion_rate = calculate_conversions(opportunities, customers)
rating = evaluate_conversions(conversion_rate)

print("Conversion rate:", conversion_rate)
print("Rating:", rating)
