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

        print(f"\n\nGenerating a Quiz that contains {number_of_questions} {assessment_type} Questions...\n\n")
        assessment = ""

        formatted_learning_outcomes = "\n".join(learning_outcomes)

        # Create a new index
        documents = SimpleDirectoryReader(r"media\upload").load_data()
        index = VectorStoreIndex.from_documents(documents)

        prompt = """
            Query string here.

            ${gr.xml_prefix_prompt}

            ${output_schema}

            ${gr.json_suffix_prompt_v2_wo_none}
        """
        # Create a guard object
        guard = gd.Guard.from_pydantic(output_class=Response, prompt=prompt)

        # Create output parse object
        output_parser = GuardrailsOutputParser(guard)


        fmt_qa_tmpl = output_parser.format(DEFAULT_TEXT_QA_PROMPT_TMPL)
        fmt_refine_tmpl = output_parser.format(DEFAULT_REFINE_PROMPT_TMPL)

        qa_prompt = PromptTemplate(fmt_qa_tmpl, output_parser=output_parser)
        refine_prompt = PromptTemplate(fmt_refine_tmpl, output_parser=output_parser)

        query_engine = index.as_query_engine(
            text_qa_template=qa_prompt,
            refine_template=refine_prompt,
        )
        
        response = query_engine.query(f"Generate 20 questions that will be able to assess if the student learned these learning outcomes: \n\n {formatted_learning_outcomes}\n\n")
        print(response)

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