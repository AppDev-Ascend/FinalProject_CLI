## Setup 
1. **Setup your ChatGPT API Key:**
   - Open the command prompt in your project directory and enter the following command:
     ```bash
     setx OPENAI_API_KEY "your-api-key-here"
     ```
     This command creates an environmental variable named OPENAI_API_KEY. Please contact me to obtain our API Key. 
     (Note: Do not include the API Key in the code repository for security reasons.)

2. **Install the required dependencies:**
   - Make sure to install the necessary dependencies by running the following command:
     ```bash
     pip install -r requirements.txt
     ```
     This command installs the required packages listed in the `requirements.txt` file. Ensure that you have the appropriate permissions and are in the correct virtual environment before running this command.

3. **Install Tesseract OCR:**
   - Download and install Tesseract OCR from the [official Tesseract GitHub page](https://github.com/tesseract-ocr/tesseract).
   - Add the directory containing `tesseract.exe` to your system's PATH for global usage.

4. **Additional Notes:**
   - If you encounter issues related to Tesseract during the project, ensure that the Tesseract executable is accessible and correctly configured in your code.

## To do (Delete this after finishing)
- [X] Add File Upload Option (.txt)
- [X] Add FIle Upload Option (.pdf)
- [X] Add PDF to Text Converter Class
- [X] Add Txt to Text Converter
- [X] Convert Assessment to a JSON
- [X] Add Saving Assessments to different File Types Class
- [X] Convert Assessment (JSON) to PDF
- [X] Convert Assessment (JSON) to GIFT
- [ ] Update JSON File
   - [ ] Check Format of New Assessment File Type
   - [ ] Update JSON to PDF for the new JSON Format
   - [ ] Update JSON to GIFT for the new JSON Format
- [ ] Update Query to Check if there are Learning Outcomes
