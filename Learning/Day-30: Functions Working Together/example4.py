def calculate_conversion_rate(leads, customers):
    return customers / leads

def calculate_cac(spend, customers):
    return spend / customers

def calculate_coverage(pipeline_amount, revenue_target):
    return pipeline_amount / revenue_target

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

def evaluate_coverage(coverage_rate):
    if coverage_rate >= 4.0:
        return "Strong"

    elif coverage_rate >= 3.0:
        return "Healthy"

    elif coverage_rate >= 2.0:
        return "At Risk"

    else:
        return "Critical"
    
def evaluate_performance(conversion_status, cac_status, coverage_status):
    if conversion_status == "Strong" and cac_status == "Efficient" and coverage_status == "Strong":
        return "Excellent"

    elif conversion_status == "Weak" or cac_status == "Expensive" or coverage_status == "Critical":
        return "Needs Attention"

    else:
        return "Healthy"

leads = int(input("Enter number of leads: "))
customers = int(input("Enter number of customers: "))
spend = int(input("Enter spend: "))
pipeline_amount = int(input("Enter pipeline amount: "))
revenue_target = int(input("Enter revenue target: "))

conversion_rate = calculate_conversion_rate(leads, customers)
conversion_status = evaluate_conversion_rate(conversion_rate)
cac = calculate_cac(spend, customers)
cac_status = evaluate_cac(cac)
coverage_rate = calculate_coverage(pipeline_amount, revenue_target)
coverage_status = evaluate_coverage(coverage_rate)
performance = evaluate_performance(conversion_status, cac_status, coverage_status)

print("Conversion rate:", conversion_rate)
print("Conversion status:", conversion_status)
print("CAC:", cac)
print("CAC status:", cac_status)
print("Coverage rate:", coverage_rate)
print("Coverage status:", coverage_status)
print("Overall performance:", performance)