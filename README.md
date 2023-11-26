# FinalProject-CLI
A repository for the CLI version of the final project. Used for testing the ChatGPT API.

## To do (Delete this after finishing)
- [ ] Add File Upload Option (.txt)
- [ ] Add FIle Upload Option (.pdf)
- [ ] Add PDF to Text Converter Class
- [ ] Add Txt to Text Converter
- [ ] Add Saving Assessments to different File Types Class
- [ ] Convert Assessment to PDF
- [ ] Convert Assessment to GIFT
- [ ] Add Different Assessment Types

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