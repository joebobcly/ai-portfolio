def score_lead(company_size, visits, demo_request):

    if company_size >= 1000 and (visits >= 10 or demo_request == "yes"):
        return "Hot"

    elif company_size >= 250 and (visits >= 5 or demo_request == "yes"):
        return "Warm"

    else:
        return "Cold"

company_size = int(input("Enter company size: "))
visits = int(input("Enter website visits: "))
demo_request = input("Requested demo? ")

status = score_lead(company_size, visits, demo_request)

print("Lead status:", status)