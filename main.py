from assessment_generator import AssessmentGenerator
from converter import Converter
import json

ai = AssessmentGenerator()

# Change the quiz filters here
type = "Multiple Choice"
question_number = 5


# Change Learning Outcomes Here
learning_outcomes = [
    "1. Identify the purpose of the Prototype Pattern.",
    "2. Understand the benefits of the Prototype Pattern"
]
assessment_json = ai.get_quiz(type, question_number, learning_outcomes)

print(f"{assessment_json}")

# Use Files to Convert
# with open(r"Project Files\assessment_exam.json", 'r') as f:
#     assessment_json = json.load(f)

# print("Converting Assessment to PDF... \n\n")
# # Save the Lesson to a PDF file
# Converter.quiz_to_pdf(assessment_json, "")

# print("Creating Answer Key... \n\n")
# Converter.quiz_answer_key(assessment_json)