from pdf2image import convert_from_path
import pytesseract
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

class Converter:
    @staticmethod
    def pdf_to_text(pdf_path):
        poppler_path = r'poppler-23.11.0\Library\bin'
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        images = convert_from_path(pdf_path, poppler_path=poppler_path)
        text = ''
        for i, img in enumerate(images):
            text += f'\nPage {i + 1}:\n\n'
            text += pytesseract.image_to_string(img, lang='eng')

        return text

    @staticmethod
    def json_to_pdf(assessment):
        # Create a PDF document
        pdf_canvas = canvas.Canvas(r"Project Files\assessment.pdf", pagesize=letter)

        # Extract information from the JSON
        assessment_type = assessment.get("type", "")
        questions = assessment.get("questions", [])
        Converter.generate_answer_key(questions)

        # Add content to the PDF
        pdf_canvas.setFont("Helvetica", 12)
        pdf_canvas.drawString(100, 800, f"Assessment Type: {assessment_type}")

        y_position = 780
        for index, question in enumerate(questions, start=1):
            y_position -= 20  # Adjust the vertical position for each question

            question_text = question.get("question", "")
            options = question.get("options", [])
            answer_index = question.get("answer", 0)

            # Add question to the PDF
            pdf_canvas.drawString(100, y_position, f"{index}. {question_text}")

            # Add options to the PDF
            for option_index, option in enumerate(options, start=1):
                y_position -= 15  # Adjust the vertical position for each option
                pdf_canvas.drawString(120, y_position, f"{chr(96 + option_index)}. {option}")

            y_position -= 20  # Adjust the vertical position for the next question

        # Save the PDF
        pdf_canvas.save()
    
    @staticmethod
    def generate_answer_key(questions):
        # Create a PDF document for the answer key
        pdf_canvas = canvas.Canvas(r"Project Files\answer_key.pdf", pagesize=letter)

        questions 

        # Add content to the PDF
        pdf_canvas.setFont("Helvetica", 12)

        y_position = 780
        for index, question in enumerate(questions, start=1):
            y_position -= 20  # Adjust the vertical position for each question

            correct_answer = f"Question {index}: {chr(96 + question['answer'])}"
            pdf_canvas.drawString(120, y_position, correct_answer)

            y_position -= 30  # Adjust the vertical position for the next question

        # Save the PDF
        pdf_canvas.save()

    def json_to_gift(assessment):
        gift_output = ""

        # Extract information from the JSON
        assessment_type = assessment.get("type", "")
        questions = assessment.get("questions", [])

        # Add a title for the assessment type
        gift_output += f"::{assessment_type}::\n\n"

        # Process each question
        for index, question in enumerate(questions, start=1):
            question_text = question.get("question", "")
            options = question.get("options", [])
            answer_index = question.get("answer", 0)

            # Add question title and text
            gift_output += f"::{index} {question_text}::\n"

            # Add options
            for option_index, option in enumerate(options, start=1):
                gift_output += f"{'=' if option_index == answer_index else '~'}{option} "

            gift_output += "\n\n"

            
            with open(r"Project Files\assessment_gift.txt", "w") as file:
                file.write(gift_output)