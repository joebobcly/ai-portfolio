name = "Joseph"
company = "SynthScale"
industry = "B2B SaaS"
goal = "Increase organic traffic by 40%"

prompt = f"""
You are an expert B2B demand generation strategist.

Company: {company}
Industry: {industry}

The marketing leader is {name}.

Primary goal:
{goal}

Provide five actionable recommendations.
"""

print(prompt)