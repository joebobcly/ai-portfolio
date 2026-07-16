name = "Joseph"
company = "SynthScale"
industry = "B2B SaaS"
audience = "Growth marketers"
goal = "Build AI agents for demand generation"
tone = "Executive"
product = "AI Growth Platform"

prompt = f"""
You are a world-class marketing strategist.

Your client is:

Company: {company}
Industry: {industry}
Audience: {audience}

The marketing leader is {name}.
The tone needs to be {tone}.
The product is {product}.

Business goal:
{goal}

Generate:

1. Three campaign ideas
2. One LinkedIn post
3. One email subject line
4. One CTA
"""

print(prompt)