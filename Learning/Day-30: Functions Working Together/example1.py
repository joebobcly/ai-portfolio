def calculate_conversion_rate(leads, customers):
    return customers / leads

def evaluate_conversion_rate(rate):
    if rate >= 0.20:
        return "Strong"

    elif rate >= 0.10:
        return "Average"

    else:
        return "Weak"

leads = 200
customers = 30

conversion_rate = calculate_conversion_rate(leads, customers)
conversion_status = evaluate_conversion_rate(conversion_rate)