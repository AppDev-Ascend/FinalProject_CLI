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

    def get_exam(self, lesson, exam_format, learning_outcomes) -> dict:
        """
        Generate an exam based on the specified format and learning outcomes.

        Parameters:
        - lesson (str): The lesson for which the exam is generated.
        - exam_format (list): A list of tuples specifying the sections of the exam.
          Each tuple contains:
            - section_name (str): The name of the exam section.
            - assessment_type (str): The type of assessment for the section (e.g., "Multiple Choice").
            - question_count (int): The number of questions to generate for the section.
        - learning_outcomes (list): A list of learning outcomes to guide question generation.

        Returns:
        dict: The generated exam in dictionary format.

        Note:
        - For testing purposes, there is a sleep of 60 seconds between generating sections
          to comply with OpenAI API usage limits (3 requests per minute on a free account).
        - The generated exam is also saved to a JSON file named 'assessment_exam.json'.
        """
         
        print("Generating an exam...\n\n")

        exam = {
            "type": "Exam",
            "sections": []
        }

        for section in exam_format:
            section_name, assessment_type, question_count = section

            print(f"Generating Section {section_name}...\n\n")

            # 
            questions = self.get_quiz(lesson, assessment_type, question_count, learning_outcomes)
            exam["sections"].append({
                "section_name": section_name,
                "section_type": assessment_type,
                "questions": questions
            })

            # for testing purposes, since OpenAI has a limit of 3 requests per minute on a free account
            time.sleep(20)
            
        return exam
    