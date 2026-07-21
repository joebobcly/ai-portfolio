def ai_prompt(industry, audience, goal):
    return f"You are an AI assistant helping a company in the {industry} industry.\nTarget audience: {audience}\nYour task is to {goal}."
    
user_industry = input("Enter your industry: ")
user_audience = input("Enter your audience: ")
user_goal = input("Enter your goal: ")

prompt = ai_prompt(user_industry, user_audience, user_goal)

print(prompt)