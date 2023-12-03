from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import time

class AI:

    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def get_assessment_quiz(self, lesson, assessment_type, number_of_questions, learning_outcomes) -> dict:
        print(f"\n\nGenerating a {assessment_type} Quiz...\n\n")
        assessment = ""
        
        match(assessment_type):
            case "Multiple Choice":
                json_data = {
                    "type": "Multiple Choice",
                    "questions": [
                    {
                        "question": "Question",
                        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
                        "answer": 1,
                    }
                    ]
                }
            case "Identification":
                json_data = {
                    "type": "Identification",
                    "questions": [
                    {
                        "question": "Question",
                        "answer": "Answer 1",
                    }
                    ]
                }
            case "True or False":
                json_data = {
                    "type": "True or False",
                    "questions": [
                    {
                        "question": "Question",
                        "answer": True,
                    }
                    ]
                }
            case "Fill in the Blanks":
                json_data = {
                    "type": "Fill in the Blanks",
                    "questions": [
                    {
                        "question": "Question is ___",
                        "answer": "Answer 1",
                    }
                    ]
                }
            case "Essay":
                json_data = {
                    "type": "Essay",
                    "questions": [
                    {
                        "question": "Question",
                    }
                    ]
                }
            case _:
                print("Error: Invalid Assessment Type")
                exit()

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
                            "content": f"You are an assessment generator who have no outside knowledge and must only generate questions based on the outputted lesson. The assessment generated should follow these learning outcomes: \n {learning_outcomes}\
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

    def get_assessment_exam(self, lesson, exam_format, learning_outcomes) -> dict:

        print("Generating an exam...\n\n")

        exam = {
            "type": "Exam",
            "sections": []
        }

        for section in exam_format:
            section_name, assessment_type, question_count = section

            print(f"Generating Section {section_name}...\n\n")

            questions = self.get_assessment_quiz(lesson, assessment_type, question_count, learning_outcomes)
            exam["sections"].append({
                "section_name": section_name,
                "section_type": assessment_type,
                "questions": questions
            })


            # for testing purposes, since OpenAI has a limit of 3 requests per minute on a free account
            time.sleep(60)

        # Save exam to a json file
        with open(f'assessment_exam.json', 'w') as f:
            json.dump(exam, f)
        
        return exam
    