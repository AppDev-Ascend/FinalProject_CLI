from assessment_generator import AI
from converter import Converter
import json

print("Assessment Generator CLI")

# user_input["Lesson"] = input("Enter Lesson: ")
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

# print("Converting Lesson to Text... \n\n")

# assessment_type = input("Enter Type of Assessment: ")
# question_number = int(input("Enter Number of Questions: "))

# number_of_outcomes = int(input("Enter Number of Learning Outcomes: "))
# learning_outcomes = ""
# for i in range(number_of_outcomes):
#     outcome = input(f"Enter Learning Outcome #{i+1}: ")
#     learning_outcomes += f"{i+1}. {outcome}\n"

lesson_in_text = Converter.pdf_to_text(r"Project Files\Prototype Pattern Document.pdf")

with open(r"Project Files\output.txt", 'r') as f:
    lesson_in_text = f.read()

learning_outcomes = [
    "1. Identify the components of the Prototype Pattern",
    "2. Understand the advantages and disadvantages of the Prototype Pattern",
]

exam_format = [
    ("Test 1", "Identification", 1),
    ("Test 2", "Multiple Choice", 2),
    ("Test 3", "True or False", 3),
    ("Test 4", "Fill in the Blanks", 2),
    ("Test 5", "Essay", 1),
]

ai = AI()

assessment_json = ai.get_exam(lesson_in_text, exam_format, learning_outcomes) 

# print(f"{assessment_json}")

with open(r"Project Files\assessment_exam.json", 'r') as f:
    assessment_json = json.load(f)

print("Converting Assessment to PDF... \n\n")
# Save the Lesson to a PDF file
Converter.exam_to_pdf(assessment_json)
print("Creating Answer Key... \n\n")
Converter.exam_answer_key(assessment_json)