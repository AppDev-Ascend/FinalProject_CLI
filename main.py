from assessment_generator import AssessmentGenerator
from converter import Converter
import json

ai = AssessmentGenerator()

# Change the quiz filters here
type = "Multiple Choice"
question_number = 5


# Change Learning Outcomes Here
learning_outcomes = [
    "Understand the concept and usage of the Prototype Design Pattern",
    "Explain the benefits and drawbacks of using the Prototype Design Pattern"
]

# Generate Assessment with no index
# assessment_json = ai.get_quiz(lesson, type, question_number, learning_outcomes)

# Generate Assessment with index
assessment_json = ai.get_quiz(type, question_number, learning_outcomes)


# Test the Converter
# with open(r"Project Files\quiz_Identification.json", 'r') as f:
#     assessment_json = json.load(f)

# print("Converting Assessment to PDF... \n\n")
# # Save the Lesson to a PDF file
# Converter.quiz_to_pdf(assessment_json, "Indentification")

# print("Creating Answer Key... \n\n")
# Converter.quiz_answer_key(assessment_json, "Identification")