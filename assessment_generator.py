from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)



rules = {
    "Type of Assesment": "Multiple Choice",
    "Number of Questions": 2,
    "Topic": "History"
}


# API Call
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
        "role": "system", 
        "content": f"You are an assessment generator. You are given a a c and you must generate an assessment for it. \
                    You must output the the assessment in JSON format.\
                    "
    },
    {"role": "user", "content": "Compose an assessment for this {rules}"}
  ]
)


# Generate Result
print(completion.choices[0].message)