from assessment_generator import AI
from converter import Converter
import json

print("Assessment Generator CLI")

# # user_input["Lesson"] = input("Enter Lesson: ")
# print("1. Text")
# print("2. PDF")
# print("3. Txt File")
# lesson_upload = input("Enter the number of the way you want to input the lesson: ")

# if lesson_upload == "1":
#     lesson_in_text = input("Enter Lesson: ")
# elif lesson_upload == "2":
#     lesson_pdf = input("Enter Lesson PDF Absolute File Path: ")
#     lesson_in_text = Converter.pdf_to_text(lesson_pdf)
# elif lesson_upload == "3":
#     lesson_txt = input("Enter Lesson TXT Absolute File Path: ")
#     with open(lesson_txt, 'r') as f:
#         lesson_in_text = f.read()
# else:
#     exit()

# assessment_type = input("Enter Type of Assessment: ")
# question_number = int(input("Enter Number of Questions: "))

# number_of_outcomes = int(input("Enter Number of Learning Outcomes: "))
# learning_outcomes = ""
# for i in range(number_of_outcomes):
#     outcome = input(f"Enter Learning Outcome #{i+1}: ")
#     learning_outcomes += f"{i+1}. {outcome}\n"


# ai = AI()

# # Generate the Lesson
# assessment_json = ai.get_assessment(lesson_in_text, assessment_type, question_number, learning_outcomes)

# print(f"Assessment Type: {assessment_json['type']}")

# For testing purposes, we will use the sample assessment
with open('assessment.json', 'r') as f:
    # Load the JSON data
    assessment_json = json.load(f)

# Save the Lesson to a PDF file
Converter.json_to_pdf(assessment_json)

# Save the Lesson to a GIFT file
Converter.json_to_gift(assessment_json)