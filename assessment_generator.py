from openai import OpenAI
from dotenv import load_dotenv
import os

class AI:

    def __init__(self):
      # Load environment variables from .env file
      load_dotenv()
      OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
      client = OpenAI(api_key=OPENAI_API_KEY)


    def get_assessment(self, assessment_type, number_of_questions, lesson) -> dict:

      match assessment_type:

        case "Multiple Choice":
          json = {
            "type": "Multiple Choice",
            "questions": [
              {
                "question": "Question 1",
                "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                "answer": "Option 1"
              },]
          }
        case "Identification":
          json = {
            "type": "Identification",
            "questions": [
              {
                "question": "Question 1",
                "answer": "Answer 1"
              },]
          }
        case "True or False":
          json = {
            "type": "True or False",
            "questions": [
              {
                "question": "Question 1",
                "answer": "Answer 1"
              },]
          }
        case "Fill in the blanks":
          json = {
            "type": "Fill in the blanks",
            "questions": [
              {
                "question": "Question 1",
                "answer": "Answer 1"
              },]
          }
        case _:
          print('Invalid Assessment Type')

      # API Call
      completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {
              "role": "system", 
              "content": f"You are an assessment generator. You are given a a c and you must generate an assessment for it. \
                          You must output the the assessment in JSON format.\
                          "
          },
          {"role": "user", "content": "Compose an assessment for this {lesson} using {assessment_type} with {number_of_questions} questions. \
                                        The output must be in this format {json}" }
        ]
      )

      # Generate Result
      print(completion.choices[0].message)





