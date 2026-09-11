# Langchain tools

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import tool
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model = ChatGoogleGenerativeAI(
    model = 'gemini-3.6-flash',
    google_api_key = api_key
)
@tool
def add(a:float , b:float)->float:
    """This function add two numbers."""
    return a+b
@tool
def subtract(a:float , b:float)->float:
    """This function is used to perform subtraction."""
    return b-a
@tool
def multiply(a:float , b:float , c:float)->float:
    """This function is used to perform multiplication."""
    return a*b*c
@tool
def division(a:float , b:float)->float:
    """This function is used to perform division."""
    return b/a
tools = [add , subtract , multiply , division]
model_with_tools = model.bind_tools(tools)
response = model_with_tools.invoke("What is 20/10")
print(response)
