from typesafe_sdk import Choice, Noul, Score, TypeSafeClient
from dotenv import load_dotenv
load_dotenv()
client = TypeSafeClient()

ticket = "Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing. I'm losing sales. Please help ASAP."
questions = {
    "department": Choice(
        instructions="Which team should handle this",
        criteria={
            "billing": "Payment or subscription issues",
            "technical": "Bugs or integration problems",
            "sales": "Pricing or account questions",
        },
    ),
    "frustration": Score(
        instructions="How frustrated the customer appears",
        criteria=[
            "Calm, just stating facts",
            "Frustrated but civil",
            "Very angry, strong language",
        ],
    ),
    "is_urgent": Noul(
        instructions="The message conveys urgency or time-sensitivity",
    ),
}
response = client.system_one(
    state=ticket,
    questions=questions,
)

print("Hello World: Jev Latest")
print("------------------")
print("Ticket:", ticket)
print("Criteria:")
for key, question in questions.items():
    print(f"- {key}: {question}")
print("------------------")
print("Results:")
print("- Department:", response.answers["department"].choice)  # "billing"
print("- Frustration:", response.answers["frustration"].score)  # 1.035
print("- Is Urgent:", response.answers["is_urgent"].noul)     # 0.999