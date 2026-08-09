from config import client


def categorize_expense(description):
    prompt = f"""
You are an expense categorization assistant.

Choose ONLY one category from this list:

Food
Transport
Shopping
Bills
Entertainment
Income
Fuel
Healthcare
Other

Expense:
{description}

Return ONLY the category name.
"""

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()