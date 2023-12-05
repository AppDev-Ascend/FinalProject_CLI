from assessment_generator import AI
from converter import Converter
import json


print("")


learning_outcomes = [
    "1. Identify the purpose of the Prototype Pattern.",
]

ai = AI()

assessment_json = ai.get_quiz("Multiple Choice", 2, learning_outcomes)
# assessment_json = ai.get_exam(lesson_in_text, exam_format, learning_outcomes) 

print(f"{assessment_json}")

# with open(r"Project Files\assessment_exam.json", 'r') as f:
#     assessment_json = json.load(f)

print("Converting Assessment to PDF... \n\n")
# Save the Lesson to a PDF file
Converter.quiz_to_pdf(assessment_json, "")
print("Creating Answer Key... \n\n")
Converter.quiz_answer_key(assessment_json)