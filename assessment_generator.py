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
        print("\n\nGenerating Assessment...\n\n")
        assessment = ""

        
        json_data = {
            "questions": [
            {
                "type": "Multiple Choice",
                "question": "Question",
                "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                "answer": 1,
            },
            {
                "type": "Identification",
                "question": "Question",
                "answer": "Answer 1"
            },
            {
                "type": "True or False",
                "question": "Question",
                "answer": True
            },
            {
                "type": "Fill in the Blanks",
                "question": "Question is ___",
                "answer": "Answer 1"
            }
            ]
        }

        json_string = json.dumps(json_data)

        is_valid = False
        while not is_valid:
            # API Call to Generate Assessment
            if json_data is not None:
                completion = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": f"You are an assessment generator. You are given a lesson and you must generate an assessment for it following these learning outcomes: \n {learning_outcomes}\
                                        Lastly, You must output the assessment in JSON format."
                        },
                        {
                            "role": "user",
                            "content": f"Compose an assessment for this lesson {lesson}. \n \
                                        The assessment should consist of {number_of_questions} {assessment_type} questions \n \
                                        Lastly, the output must be a JSON in this format: {json_string}"
                        }
                    ]
                )

                assessment = completion.choices[0].message.content
                print(f"Assessment: {assessment}")

                # Test the Assessment Format
                try:
                    assessment_json = json.loads(assessment)
                    print(f"Assessment Json: {assessment_json}")

                    if "questions" in assessment_json and isinstance(assessment_json["questions"], list):
                        for question in assessment_json["questions"]:
                            if "type" in question and "question" in question:
                                is_valid = True
                            else:
                                print("Error: Question in the assessment does not match expected format.")
                                is_valid = False
                                break
                    else:
                        print("Error: Assessment JSON structure does not match expected format.")
                        is_valid = False

                except json.JSONDecodeError:
                    print(assessment_json)
                    print("Error: Assessment is not in valid JSON format")
                    is_valid = False

                is_valid = True
        # Save assessment to a json file
        with open('assessment.json', 'w') as f:
            json.dump(assessment_json, f)

        return assessment_json