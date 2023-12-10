from assessment_generator import AssessmentGenerator
from converter import Converter
import json
import time

ai = AssessmentGenerator()

# Change the quiz filters here
# type = "Multiple Choice"
# type = "Identification"
# type = "True or False"
# type = "Fill in the Blanks"
type = "Essay"

question_number = 10


# Change Learning Outcomes Here
learning_outcomes = [
    "Understand what the Prototype Design Pattern is and how it is used in software development",
    "Understand the concept and usage of the Prototype Design Pattern",
    "Explain the benefits and drawbacks of using the Prototype Design Pattern"
]

# Generate a Quiz
start_time = time.time()
assessment_json = ai.get_quiz(type, question_number, learning_outcomes, lesson="")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

# Generate an Exam

# exam_format = [
#     ("Test 1", "Multiple Choice", 10),
#     ("Test 2", "Identification", 10),
#     ("Test 3", "True or False", 10),
#     ("Test 4", "Fill in the Blanks", 10),
#     ("Test 5","Essay", 10)
# ]

# # Start timer
# start_time = time.time()

# assessment_json = ai.get_exam(exam_format, learning_outcomes)

# # End timer
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time} seconds")

# Test the Converter
# with open(r"Project Files\quiz_Identification.json", 'r') as f:
#     assessment_json = json.load(f)

# print("Converting Assessment to PDF... \n\n")
# # Save the Lesson to a PDF file
# Converter.quiz_to_pdf(assessment_json, "Indentification")

# print("Creating Answer Key... \n\n")
# Converter.quiz_answer_key(assessment_json, "Identification")