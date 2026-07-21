def build_prompt(role, task):
    return f"You are a {role}. Your job is to {task}."

user_role = input("Enter a role: ")
user_role = input("Enter a task: ")

prompt = build_prompt(user_role, user_task)

print(prompt)