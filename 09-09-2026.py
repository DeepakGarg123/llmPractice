# connecting Langchain with gemini

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)

response = model.invoke(
    "Explain LangChain in simple words and also give me a real life example."
)

print(response.content[0]['text'])

# System message , Human Message

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage , SystemMessage
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
model = ChatGoogleGenerativeAI(
    model = 'gemini-3.6-flash',
    google_api_key = api_key
)
messages = [
    SystemMessage(
        content="You are a Python Tutor."
    ),
    HumanMessage(
        content="Explain decorators in Python."
    )
]
response = model.invoke(messages)
print(response.content[0]['text'])

# Prompt Template

import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
model = ChatGoogleGenerativeAI(
    model = 'gemini-3.6-flash',
    google_api_key = api_key
)
prompt= PromptTemplate.from_template(
    "Explain {topic} in simple words to a {level} student."
)
formatted_prompt = prompt.invoke({
    "topic"  : 'Python',
    "level"  : 'beginner'
})
response = model.invoke(formatted_prompt)
print(response.content[0]['text'])
with open('response.json' , 'w') as f:
    json.dump(response.content[0]['text'] , f , indent=4)











