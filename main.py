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

# print("Converting Lesson to Text... \n\n")

# # lesson_in_text = Converter.pdf_to_text(r"Project Files\Prototype Pattern Document.pdf")

# with open(r"Project Files\output.txt", 'r') as f:
#     lesson_in_text = f.read()



# ai = AI()

# assessment_json = ai.get_assessment_quiz(lesson_in_text, "Fill in the Blanks", 2, learning_outcomes) 

# print(f"{assessment_json}")

# For testing purposes, we will use the sample assessment
with open(f'Project Files/assessment_Multiple Choice.json', 'r') as f:
    # Load the JSON data
    assessment_json = json.load(f)

# Save the Lesson to a PDF file
Converter.json_to_pdf(assessment_json)