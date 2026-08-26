def calculate_conversion_rate(leads, customers):
    return customers / leads

def calculate_cac(spend, customers):
    return spend / customers

def evaluate_conversion_rate(rate):
    if rate >= 0.20:
        return "Strong"

    elif rate >= 0.10:
        return "Average"

    else:
        return "Weak"

def evaluate_cac(cac):
    if cac <= 500:
        return "Efficient"

    elif cac <=1000:
        return "Acceptable"

    else:
        return "Expensive"

leads = 200
customers = 30
spend = 12000

conversion_rate = calculate_conversion_rate(leads, customers)
conversion_status = evaluate_conversion_rate(conversion_rate)
cac = calculate_cac(spend, customers)
cac_status = evaluate_cac(cac)

print("Conversion rate:", conversion_rate)
print("Conversion status:", conversion_status)
print("CAC:", cac)
print("CAC status:", cac_status)