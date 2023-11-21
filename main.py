from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


pattern_description = """
Overview:
The Prototype Design Pattern is a creational design pattern that focuses on creating objects by copying an existing object, known as the prototype. This pattern is particularly useful when the cost of creating an object is more expensive or complex than copying an existing one. In essence, it allows for the creation of new objects by duplicating an existing one, serving as a blueprint for the new instances.

Learning Objectives:
1. Understand the motivation behind the Prototype Design Pattern.
2. Learn the structure and participants involved in the Prototype Design Pattern.
3. Implement a basic example to demonstrate the usage of the Prototype Design Pattern in a programming language.

Motivation:
- Object Creation Cost: Sometimes, the cost of creating a new object is high, involving complex initialization processes or resource-intensive operations. In such cases, creating an object by copying an existing one can be more efficient.
- Dynamic Object Creation: The Prototype pattern allows for dynamic creation of objects at runtime by copying an existing object. This can be useful when the exact type of the object is not known until runtime.

Structure:
Prototype:
- Declares an interface for cloning itself.
- Usually, this is an abstract class or an interface that concrete prototypes will implement.

ConcretePrototype:
- Implements the Clone method declared in the Prototype.
- Represents the object that can be cloned.

Client:
- Creates new objects by requesting cloning from the prototype.

Implementation Steps:
Step 1: Define the Prototype Interface
python
Copy code
# prototype.py
from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

Step 2: Implement Concrete Prototypes
python
Copy code
# concrete_prototypes.py
from prototype import Prototype

class ConcretePrototype1(Prototype):
    def clone(self):
        return ConcretePrototype1()

class ConcretePrototype2(Prototype):
    def clone(self):
        return ConcretePrototype2()

Step 3: Implement the Client
python
Copy code
# client.py
from concrete_prototypes import ConcretePrototype1, ConcretePrototype2

class Client:
    def __init__(self):
        self.prototype1 = ConcretePrototype1()
        self.prototype2 = ConcretePrototype2()

    def create_objects(self):
        clone1 = self.prototype1.clone()
        clone2 = self.prototype2.clone()

if __name__ == "__main__":
    client = Client()
    client.create_objects()

Conclusion:
The Prototype Design Pattern is a powerful tool for creating objects efficiently, especially in scenarios where the cost of object creation is high. By providing a mechanism for object cloning, it promotes flexibility and dynamic object creation at runtime. Understanding and applying this pattern can lead to more maintainable and scalable code.
"""

user_input = {
    "Lesson": pattern_description,
    "Type of Assesment": "Multiple Choice",
    "Number of Questions": 2,
}


# True or False, Identification, Fill in the Blanks
# Format of the JSON
# Safeguard JSON format


# API Call
completion = client.chat.completions.create(
  model="gpt-4-1106-preview",
  messages=[
    {
        "role": "system", 
        "content": f"You are an assessment generator. You are given a a c and you must generate an assessment for it. \
                    You must output the the assessment in JSON format.\
                    "
    },
    {
        "role": "user", 
        "content": "Compose an assessment for this topic {user_input['Lesson']}. \
                    The number of questions should be {user_input['Number of Questions'] \
                    and the type of assessment should be {user_input['Type of Assesment']"
    }
  ]
)


# Generate Result
print(completion.choices[0].message)