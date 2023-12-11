from dotenv import load_dotenv
import openai
import os
import json
import time
from llama_index import VectorStoreIndex, SimpleDirectoryReader, Prompt
class AssessmentGenerator:
    
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")


    def read_excluded_questions(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return f.read()
        else:
            return ""
    
    def write_excluded_questions(self, file_path, questions):
        with open(file_path, 'w') as f:
            f.write(questions)

    def get_quiz(self, assessment_type, number_of_questions, learning_outcomes, lesson="", exclude_questions=False, index=None) -> dict:
        
        assessment = ""

        if index is None:
            if lesson == "":
                print("Loading the Documents")
                documents = SimpleDirectoryReader(r"media\lessons").load_data()
            else:
                print("Storing the Lesson")
                with open(r'media\lessons\lesson.txt', 'w') as f:
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
                                    "answer": Int Index \
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
                                Do not include numbers in the questions. Separate each question with a new line.\n\
                                Respond only with the output in the exact format specified, with no explanation or conversation.'

            case "Fill in the Blanks" | "fill in the blanks":
                question = "fill in the blanks questions with important terms as an answer"
                response_format = 'The result type should be provided in the following JSON data structure:\n\
                                {\
                                    "question": "Question with blank", \
                                    "answer": "Answer" \
                                }\n\
                                Do not include numbers in the questions. Separate each question with a new line.\n\
                                Respond only with the output in the exact format specified, with no explanation or conversation.'
            case "Essay" | "essay":
                question = "essay questions"
                response_format = 'The result type should be provided in the following JSON data structure:\n\
                                { \
                                    "question": "Question", \
                                }\n\
                                Do not include numbers in the questions. Separate each question with a new line.\n\
                                Respond only with the output in the exact format specified, with no explanation or conversation.'
            case _:
                pass                        

        # Format for the prompt
        if learning_outcomes == []:
            my_prompt = f"Generate {number_of_questions} {question}.\n\n{response_format}"
        else:
            formatted_learning_outcomes = "\n".join(learning_outcomes)
            my_prompt = f"Generate {number_of_questions} {question} that is aligned with these learning outcomes: \n\n {formatted_learning_outcomes}\n\n.{response_format}"
        
        if exclude_questions:
            my_prompt = my_prompt + "\n\n. Make sure the questions that are in the context are excluded.{response_format}"
        
        query_engine = index.as_query_engine()
        assessment = query_engine.query(my_prompt)
      
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

        with open(fr'media\assessments\quiz_{assessment_type.lower().replace(" ", "_")}.json', 'w') as f:
            json.dump(quiz, f)
        
        return quiz
    
    def get_exam(self, exam_format, lesson="") -> dict:

        if lesson == "":
            documents = SimpleDirectoryReader(r"media\lessons").load_data()
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
            section_name, assessment_type, question_count, learning_outcomes = section
            
            # Can be removed if we moved to a better api
            time.sleep(20)

            questions = self.get_quiz(assessment_type, question_count, learning_outcomes, exclude_questions=False, index=index)
            

            exam["sections"].append({
                "name": section_name,
                "type": assessment_type,
                "questions": questions["questions"]
            })

            # # Add excluded questions
            # excluded_questions_file_path = r'media\lessons\excluded_questions.txt'
            # existing_excluded_questions = self.read_excluded_questions(excluded_questions_file_path)

            # for question in questions["questions"]:
            #     existing_excluded_questions = existing_excluded_questions + "\n" + question["question"]
            # self.write_excluded_questions(excluded_questions_file_path, existing_excluded_questions)

            
        # self.write_excluded_questions(excluded_questions_file_path, "")

        # Save exam to a json file
        with open(fr'media\assessments\exam.json', 'w') as f:
            json.dump(exam, f)
        
        return exam