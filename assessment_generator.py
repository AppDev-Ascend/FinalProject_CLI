from dotenv import load_dotenv
import openai
import os
import json
import time
from llama_index import VectorStoreIndex, SimpleDirectoryReader, Prompt

# For Persistent Data, used for testing only
from llama_index import StorageContext, load_index_from_storage

from llama_index.program import OpenAIPydanticProgram
from pydantic import BaseModel
from llama_index.llms import OpenAI
from llama_index.callbacks import OpenAIFineTuningHandler
from llama_index.callbacks import CallbackManager
from typing import List


class Question(BaseModel):
    question: str
    options: List[str]
    answer: int

class Quiz(BaseModel):
    type: str
    questions: List[Question]

class Section(BaseModel):
    section_name: str
    section_type: str
    questions: List[Question]

class Exam(BaseModel):
    type: str
    sections: List[Section]



class AssessmentGenerator:

    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_quiz(self, assessment_type, number_of_questions, learning_outcomes, lesson="", exclude_questions=False, index=None) -> dict:
        
        print(f"\n\nGenerating a Quiz that contains {number_of_questions} {assessment_type} questions...\n\n")
        assessment = ""

        formatted_learning_outcomes = "\n".join(learning_outcomes)

        if(index is None):
            if lesson == "":
                documents = SimpleDirectoryReader(r"media\upload").load_data()
            else:
                with open(r'media\upload\lesson.txt', 'w') as f:
                    f.write(lesson)
                documents = SimpleDirectoryReader(lesson).load_data()

            index = VectorStoreIndex.from_documents(documents)
        

        # Create response format
        match(assessment_type):
            case "Multiple Choice" | "multiple choice":
                question = "multiple choice questions with important terms as an answer"
                response_format = 'The result type should be provided in the following JSON data structure:\n\
                                {\
                                    "question": "Question", \
                                    "options": ["Option 1", "Option 2", "Option 3", "Option 4"], \
                                    "answer": "Index" \
                                }\n\
                                Separate each question with a new line.\n\
                                Respond only with the output in the exact format specified, with no explanation or conversation.'

            case "Identification" | "identification" | "True or False" | "true or false":
                question = "identification questions where answers are important terms" if assessment_type == "Identification" else "true or false questions"
                response_format = 'The result type should be provided in the following JSON data structure:\n\
                                {\
                                    "question": "Question", \
                                    "answer": "Answer" \
                                }\n\
                                Separate each question with a new line.\n\
                                Respond only with the output in the exact format specified, with no explanation or conversation.'

            case "Fill in the Blanks" | "fill in the blanks":
                question = "fill in the blanks questions with important terms as an answer"
                response_format = 'The result type should be provided in the following JSON data structure:\n\
                                {\
                                    "question": "Question with blank", \
                                    "answer": "Answer" \
                                }\n\
                                Separate each question with a new line.\n\
                                Respond only with the output in the exact format specified, with no explanation or conversation.'
            case "Essay" | "essay":
                question = "essay questions"
                response_format = 'The result type should be provided in the following JSON data structure:\n\
                                { \
                                    "question": "Question", \
                                }\n\
                                Separate each question with a new line.\n\
                                Respond only with the output in the exact format specified, with no explanation or conversation.'
            case _:
                print("Invalid Assessment Type")                        

        # Format for the prompt
        if exclude_questions:
            my_prompt = f"Generate {number_of_questions} {question} that will assess students with these learning outcomes: \n\n {formatted_learning_outcomes}\n\n. Make sure the questions that are in the context are excluded.{response_format}"
        else:
            my_prompt = f"Generate {number_of_questions} {question} that will assess students with these learning outcomes: \n\n {formatted_learning_outcomes}\n\n.{response_format}"
        
        query_engine = index.as_query_engine(response_mode="compact")
        assessment = query_engine.query(my_prompt)
        
        print(assessment) 

        # Convert to JSON
        assessment_str = str(assessment)
        lines = assessment_str.splitlines()
        quiz = {
            "type": assessment_type,
            "questions": []
        }

        for line in lines:
            if line != "":
                question = json.loads(line)
                quiz["questions"].append(question)

        # Save the JSON data to a file
        with open(fr'media\assessments\quiz_{assessment_type.lower().replace(" ", "_")}.json', 'w') as f:
            json.dump(quiz, f)
        
        return quiz
    
    def get_exam(self, exam_format, learning_outcomes, lesson="") -> dict:
        
        print("Generating an exam...\n\n")

        if lesson == "":
            documents = SimpleDirectoryReader(r"media\upload").load_data()
        else:
            with open(r'media\upload\lesson.txt', 'w') as f:
                f.write(lesson)
            documents = SimpleDirectoryReader(lesson).load_data()

        index = VectorStoreIndex.from_documents(documents)

        exam = {
            "type": "Exam",
            "sections": []
        }

        excluded_questions = ""

        for section in exam_format:
            
            # Can be removed if we moved to a better api
            time.sleep(20)

            section_name, assessment_type, question_count = section

            print(f"Generating {section_name}...\n\n")
            questions = self.get_quiz(assessment_type, question_count, learning_outcomes, exclude_questions=True, index=index)
            
            exam["sections"].append({
                "section_name": section_name,
                "section_type": assessment_type,
                "questions": questions
            })

            # Add excluded questions
            # Define the path to the excluded questions file
            excluded_questions_file_path = r'media\upload\excluded_questions.txt'

            # Check if the file exists
            if os.path.exists(excluded_questions_file_path):
                # Read existing excluded questions
                with open(excluded_questions_file_path, 'r') as f:
                    existing_excluded_questions = f.read()
            else:
                # If the file doesn't exist, start with an empty string
                existing_excluded_questions = ""

            # Add new questions to the excluded list
            for question in questions["questions"]:
                existing_excluded_questions += question["question"] + "\n"

            # Write the updated excluded questions back to the file
            with open(excluded_questions_file_path, 'w') as f:
                f.write(existing_excluded_questions)

        # Save exam to a json file
        with open(fr'media\exam.json', 'w') as f:
            json.dump(exam, f)
        
        return exam