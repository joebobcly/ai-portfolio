def calculate_coverage(pipeline_amount, revenue_target):
    coverage_rate = pipeline_amount / revenue_target
    return coverage_rate

def evaluate_coverage(coverage_rate):

    if coverage_rate >= 4.0:
        return "Strong"

    elif coverage_rate >= 3.0:
        return "Healthy"

    elif coverage_rate >= 2.0:
        return "At Risk"

    else:
        return "Critical"

pipeline_amount = int(input("Enter pipeline amount: "))
revenue_target = int(input("Enter revenue target: "))

coverage_rate = calculate_coverage(pipeline_amount, revenue_target)
status = evaluate_coverage(coverage_rate)

print("Pipeline coverage:", coverage_rate)
print("Status:", status)