# Getting Started

```
python3 -m venv .venv
source ./.venv/bin/activate
pip3 install -r requirements.txt
python3 hello_world.py
```

```
Hello World: Jev Latest
------------------
Ticket: Hi, I've been trying to connect my Stripe account for 3 days and it keeps failing. I'm losing sales. Please help ASAP.
Criteria:
- department: type='choice' instructions='Which team should handle this' criteria={'billing': 'Payment or subscription issues', 'technical': 'Bugs or integration problems', 'sales': 'Pricing or account questions'}
- frustration: type='score' instructions='How frustrated the customer appears' criteria=['Calm, just stating facts', 'Frustrated but civil', 'Very angry, strong language']
- is_urgent: type='noul' instructions='The message conveys urgency or time-sensitivity' criteria=None
------------------
Results:
- Department: billing
- Frustration: 1.0
- Is Urgent: 1.0
```
