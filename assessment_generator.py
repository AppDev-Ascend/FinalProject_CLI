from openai import OpenAI
from dotenv import load_dotenv
import os
import json

class AI:

    def __init__(self):
      # Load environment variables from .env file
      load_dotenv()
      OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
      self.client = OpenAI(api_key=OPENAI_API_KEY)
      

    def get_assessment(self, lesson, assessment_type, number_of_questions, learning_outcomes) -> dict:
        
        assessment = ""

        match assessment_type:
            case "Multiple Choice":
                json_data = {
                    "type": "Multiple Choice",
                    "questions": [
                    {
                        "question": "Question 1",
                        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                        "answer": 1,
                    },]
                }
            
            case "Identification":
                json_data = {
                    "type": "Identification",
                    "questions": [
                    {
                        "question": "Question 1",
                        "answer": "Answer 1"
                    },]
                }
            case "True or False":
                json_data = {
                    "type": "True or False",
                    "questions": [
                    {
                        "question": "Question 1",
                        "answer": "Answer 1"
                    },]
                }
            case "Fill in the blanks":
                json_data = {
                    "type": "Fill in the blanks",
                    "questions": [
                    {
                        "question": "Question 1",
                        "answer": "Answer 1"
                    },]
                }
            case _:
                json_data = {}
                print('Invalid Assessment Type')

        json_string = json.dumps(json_data)

        is_valid = False
        while(not is_valid):
            # API Call
            if json_data is not None:
                completion = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {
                        "role": "system", 
                        "content": f"You are an assessment generator. You are given a lesson and you must generate an assessment for it. \
                                        You must output the the assessment in JSON format.\
                                    "
                    },
                    {
                        "role": "user", 
                        "content": f"Compose an assessment for this lesson {lesson}. \n \
                                    The assessment should consist {number_of_questions} {assessment_type} questions. \
                                    It should follow these learning outcomes: {learning_outcomes}. \n \
                                    Lastly, the output must be a JSON in this format: {json_data}" }
                    ]
                )

            # Generate Result
            assessment = completion.choices[0].message.content

            # Check if result is in the correct format
            is_valid = True

        # Convert assessment to JSON
        try:
            assessment_json = json.loads(assessment)
        except json.JSONDecodeError:
            print("Error: Assessment is not in valid JSON format")
            assessment_json = {}

        # Save assessment to a json file
        with open('assessment.json', 'w') as f:
            json.dump(assessment_json, f)

        return assessment