from pdf2image import convert_from_path
import pytesseract

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