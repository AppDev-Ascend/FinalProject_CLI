from assessment_generator import AssessmentGenerator
from converter import Converter
import time
import json

ai = AssessmentGenerator()

# Change the quiz filters here
# quiz_type = "Multiple Choice"
# quiz_type = "Identification"
# quiz_type = "True or False"
# quiz_type = "Fill in the Blanks"
# quiz_type = "Essay"

# number_of_questions = 5


# # Change Learning Outcomes Here
# learning_outcomes = [
#     "Understand what the Prototype Design Pattern is and how it is used in software development",
#     "Understand the concept and usage of the Prototype Design Pattern",
#     "Explain the benefits and drawbacks of using the Prototype Design Pattern"
# ]

# # Generate a Quiz
# start_time = time.time()
# assessment_json = ai.get_quiz(quiz_type, number_of_questions, learning_outcomes=learning_outcomes)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time} seconds")

# Generate an Exam

exam_format = [
    ("Test 1", "Multiple Choice", 5, ["Understand what the Prototype Design Pattern is and how it is used in software development"]),
    ("Test 3", "True or False", 5, ["Understand the concept and usage of the Prototype Design Pattern"]),
    ("Test 5","Essay", 3, ["Explain the benefits and drawbacks of using the Prototype Design Pattern"])
]

# Start timer
start_time = time.time()

assessment_json = ai.get_exam(exam_format)

# # End timer
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")

# Test the Converter

# Quiz
# with open(fr'media\assessments\quiz_{quiz_type.lower().replace(" ", "_")}.json', 'r') as f:
#    assessment_json = json.load(f)


# # Convert the Assessment to a PDF
# print("Converting Assessment to PDF... \n\n")
# # Save the Lesson to a PDF file
# Converter.quiz_to_pdf(assessment_json)


# print("Creating Answer Key... \n\n")
# Converter.quiz_answer_key(assessment_json)

# # Convert to a GIFT Format
# print("Converting Assessment to GIFT Format... \n\n")
# Converter.quiz_to_gift(assessment_json)

# # Convert to a Word Document
# print("Converting Assessment to Word Document... \n\n")
# Converter.quiz_to_docx(assessment_json)

# # Exam
# with open(fr'media\assessments\exam.json', 'r') as f:
#     assessment_json = json.load(f)


# Convert the Exam to a PDF
# print("Converting Exam to PDF... \n\n")
# # Save the Lesson to a PDF file
# Converter.exam_to_pdf(assessment_json)


# # print("Creating Answer Key... \n\n")
# Converter.exam_answer_key(assessment_json)

# # Convert to a GIFT Format
# print("Converting Assessment to GIFT Format... \n\n")
# Converter.exam_to_gift(assessment_json)

# # Convert to a Word Document
# print("Converting Assessment to Word Document... \n\n")
# Converter.exam_to_docx(assessment_json)