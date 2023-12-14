import os
from openai import OpenAI
OPEN_AI_KEY="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"

client = OpenAI(
    # This is the default and can be omitted
    api_key=OPEN_AI_KEY,
)

with open("server/test_data/transcript.txt", 'r') as f:
    transcript = f.read()
response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": """You will be provided with a meeting transcript, and your task is to answer the following:
What are the rep accounted for the next week?
What are the rep action items to do?
What are my action items?
Deal discussion summary and next steps and each deal $ value forecast (split this for each deal discussed)?
General call summary?

Here are some company specific definitions:
QBR: Quarterly Business Review
MCV: Monthly contract value
Burn list: A list of actions one once to do and check off
CRW: Contract re-writes. Re-negotiating current contract end date to sign a new start date in advance of the original contract's start date to secure the renewal in advance. Say client has a 12 month subscription from Feb 2023 to Feb 2024, contract rewrite would be negotiation with the client to sign the renewal for Dec 2024 to Dec 2025 and give 2 months of credit. If rep negotiates growth on the deal, the MCV is higher even with the credit.   
CKIP: Custom Key Initiative Plan. Reps run CKIPs with their clients to understand where they can add more value on selling their services
Other Environment context: Nayla is the Sales Director at an HR research advisory firm that provides leaders with practical information and applicable skills through comprehensive training resources and leadership development programs. Client pay a membership to access advisors and the McLean research portal/content.
Nayla is Manager
Edwin is the account manager with sales targets on new accounts, growth on current accounts managed, and servicing current accounts.@
great before doing so, see here the agenda the sales manager had in mind for the meeting:

Agenda for the meeting (30-45 minutes)

Forecast review - walk me through your gap for December?


How are your accounts looking for Q3 and Q4

Risks?

Quota discussion.

Want to talk about MCV and revenue for the month.

Rep should focus on deals they have and talk through strategy instead of the above details.

Everything above should be 10-15 minutes.

Talk about how last week went
      """
    },
    {
      "role": "user",
      "content": transcript
    }],
  temperature=0,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
chat_response = response.choices[0].message.content.strip()
print(chat_response)