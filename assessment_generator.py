from dotenv import load_dotenv
import openai
import os
import json
import time
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.output_parsers import GuardrailsOutputParser
from llama_index.program import OpenAIPydanticProgram

from pydantic import BaseModel, Field
from typing import List, Optional
import guardrails as gd

from llama_index.prompts import PromptTemplate
from llama_index.prompts.default_prompts import (
    DEFAULT_TEXT_QA_PROMPT_TMPL,
    DEFAULT_REFINE_PROMPT_TMPL,
)

from llama_index import StorageContext, load_index_from_storage

class Question(BaseModel):
    question: str
    options: List[str]
    answer: int

class Response(BaseModel):
    type: str
    questions: List[Question]

class AssessmentGenerator:

    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_quiz(self, assessment_type, number_of_questions, learning_outcomes) -> dict:
        
        print(f"\n\nGenerating a Quiz that contains {number_of_questions} {assessment_type} questions...\n\n")
        assessment = ""

        formatted_learning_outcomes = "\n".join(learning_outcomes)

        # Create a new index
        # For New Data
        documents = SimpleDirectoryReader(r"media\upload").load_data()
        index = VectorStoreIndex.from_documents(documents)
        
        
        # For Persistent Data, used for testing only
        index.storage_context.persist(r"media\index")
        
        # storage_context = StorageContext.from_defaults(persist_dir="<persist_dir>")
        # index = load_index_from_storage(storage_context)

        # Create response format
        match(assessment_type):
            case "Multiple Choice" | "multiple choice":
                response_format = "<Insert Question Here>\n<Insert Option 1 Here>\n<Insert Option 2 Here>\n<Insert Option 3 Here>\n<Insert Option 4 Here>\n<Insert Answer Here>"
            case "Identification" | "identification" | "True or False" | "true or false" | "Fill in the Blanks" | "fill in the blanks":
                response_format = "<Insert Question Here> \n<Insert Answer Here>"
            case "Essay" | "essay":
                response_format = "<Insert Question Here>"
                        

        # Format for the prompt
        my_prompt = f"Generate {number_of_questions} {assessment_type} questions that with these learning outcomes: \n\n {formatted_learning_outcomes}\n\n that outputs the question in this format: \n {response_format}. If there are multiple questions, separate them with one line."

        query_engine = index.as_query_engine(response_mode="compact")
        assessment = query_engine.query(my_prompt)
        
        # Test 
        print(assessment)

        # Split the string into lines
        lines = assessment.strip().split("\n")

        # The first line is the question
        question_text = lines[0][3:].strip()

        # The last line is the answer
        answer_text = lines[-1]

        # The middle lines are the options
        options = [line[3:].strip() for line in lines[1:-1]]

        # Extract the answer letter and convert it to an index
        answer_letter = answer_text.split(": ")[1]
        answer_index = ord(answer_letter) - ord('a')

        # Create the JSON data
        json_data = {
            "type": "Multiple Choice",
            "questions": [
                {
                    "question": question_text,
                    "options": options,
                    "answer": answer_index
                }
            ]
        }

        # Print the JSON data
        print(json_data)

        with open(fr'media\assessments\quiz_{assessment_type}.json', 'w') as f:
            json.dump(json_data, f)
    
        return assessment


    def get_exam(self, lesson, exam_format, learning_outcomes) -> dict:
         
        print("Generating an exam...\n\n")

        exam = {
            "type": "Exam",
            "sections": []
        }

        for section in exam_format:
            section_name, assessment_type, question_count = section

            print(f"Generating Section {section_name}...\n\n")

            questions = self.get_quiz(lesson, assessment_type, question_count, learning_outcomes)
            exam["sections"].append({
                "section_name": section_name,
                "section_type": assessment_type,
                "questions": questions
            })

            # for testing purposes, since OpenAI has a limit of 3 requests per minute on a free account
            time.sleep(20)

        # Save exam to a json file
        with open(fr'media\exam.json', 'w') as f:
            json.dump(exam, f)
        
        return exam