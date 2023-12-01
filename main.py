from assessment_generator import AI
from converter import Converter

print("Assessment Generator CLI")

# user_input["Lesson"] = input("Enter Lesson: ")
print("1. Text")
print("2. PDF")
lesson_upload = input("Enter the number of the way you want to input the lesson: ")

if lesson_upload == "1":
    lesson_in_text = input("Enter Lesson: ")
else:
    lesson_pdf = input("Enter Lesson PDF Absolute File Path: ")
    lesson_in_text = Converter.pdf_to_text(lesson_pdf)

assessment_type = input("Enter Type of Assessment: ")
question_number = int(input("Enter Number of Questions: "))

number_of_outcomes = int(input("Enter Number of Learning Outcomes: "))
learning_outcomes = [None] * number_of_outcomes
for i in range(number_of_outcomes):
    learning_outcomes[i] = input(f"Enter Learning Outcome #{i+1}: ")

ai = AI()

output_json = ai.get_assessment(lesson_in_text, assessment_type, question_number, learning_outcomes)

print(output_json)