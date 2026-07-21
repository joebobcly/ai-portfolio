def ai_prompt(industry, audience):
    return f"You are helping someone in the {industry} industry create content for {audience}."

user_industry = input("Enter your industry: ")
user_audience = input("Enter the audience: ")

prompt = ai_prompt(user_industry, user_audience)

print(prompt)