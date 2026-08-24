def classify_lead(company_size, engagement):

    if company_size >= 1000 and engagement >= 80:
        return "High Priority"

    elif company_size >= 500 and engagement >= 50:
        return "Medium Priority"

    else:
        return "Low Priority"

    result = classify_lead(750, 65)

    print(result)