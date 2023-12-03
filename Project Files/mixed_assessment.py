# For Mixed Assessment
json_data = {
    "questions": [
        {
            "type": "Multiple Choice",
            "question": "Question",
            "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
            "answer": 1,
        },
        {
            "type": "Identification",
            "question": "Question",
            "answer": "Answer 1",
        },
        {
            "type": "True or False",
            "question": "Question",
            "answer": True,
        },
        {
            "type": "Fill in the Blanks",
            "question": "Question is ___",
            "answer": "Answer 1",
        },
        {
            "type": "Essay",
            "question": "Question",
        }
    ]
}


# For the Mixed Assessment

# @staticmethod
    # def json_to_pdf2(assessment):
    #     # Create a PDF document
    #     pdf_canvas = canvas.Canvas(r"Project Files\assessment.pdf", pagesize=letter)

    #     # Extract information from the JSON
    #     questions = assessment.get("questions", [])
    #     Converter.generate_answer_key(questions)

    #     # Add content to the PDF
    #     pdf_canvas.setFont("Helvetica", 12)

    #     y_position = 780
    #     for index, question in enumerate(questions, start=1):
    #         y_position -= 20  # Adjust the vertical position for each question

    #         question_text = question.get("question", "")
    #         options = question.get("options", [])
    #         answer_index = question.get("answer", 0)

    #         # Add question to the PDF
    #         pdf_canvas.drawString(100, y_position, f"{index}. {question_text}")

    #         # Add options to the PDF
    #         for option_index, option in enumerate(options, start=1):
    #             y_position -= 15  # Adjust the vertical position for each option
    #             pdf_canvas.drawString(120, y_position, f"{chr(96 + option_index)}. {option}")

    #         y_position -= 20  # Adjust the vertical position for the next question

    #     # Save the PDF
    #     pdf_canvas.save()