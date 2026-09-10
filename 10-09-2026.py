
# Import Libraries 

# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# load_dotenv()
# api_key = os.getenv('GEMINI_API_KEY')
# model = ChatGoogleGenerativeAI(
#     model = 'gemini-3.6-flash',
#     google_api_key = api_key
# )
# prompt = ChatPromptTemplate.from_messages([
#     ("system" , "You are a Python tutor") , 
#     ("human" , "Explain {topic} in Python")]    
# )
# parser = StrOutputParser()
# chain = prompt|model|parser
# result = chain.invoke({"topic" : "Decorators"})
# print(result)

# batch part


# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# load_dotenv()
# api_key = os.getenv('GEMINI_API_KEY')
# model = ChatGoogleGenerativeAI(
#     model = 'gemini-3.6-flash',
#     google_api_key = api_key
# )
# prompt = ChatPromptTemplate.from_messages([
#     ("system" , "You are a Python tutor") , 
#     ("human" , "Explain {topic} in Python")]    
# )
# parser = StrOutputParser()
# chain = prompt|model|parser
# inputs = [{
#     "topic"  : "inheritance"
# },
# {
#     "topic"  : "Polymorphism"
# },
# {
#     "topic"  : "Inheritance"
# },
# {
#     "topic"  : "Encapsulation"
# }, 
# {
#     "topic"  : "Abstraction"
# }]

# result = chain.batch(inputs)
# print(result)

# streaming part

# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# load_dotenv()
# api_key = os.getenv('GEMINI_API_KEY')
# model = ChatGoogleGenerativeAI(
#     model = 'gemini-3.6-flash',
#     google_api_key = api_key
# )
# prompt = ChatPromptTemplate.from_messages([
#     ("system" , "You are a Python tutor") , 
#     ("human" , "Explain {topic} in Python")]    
# )
# parser = StrOutputParser()
# chain = prompt|model|parser

# for chunk in chain.stream({
#     "topic" : "inheritance"    
# }):
#     print(chunk , end="")


# async function

# import os
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# load_dotenv()
# api_key = os.getenv('GEMINI_API_KEY')
# model = ChatGoogleGenerativeAI(
#     model = 'gemini-3.6-flash',
#     google_api_key = api_key
# )
# prompt = ChatPromptTemplate.from_messages([
#     ("system" , "You are a Python tutor") , 
#     ("human" , "Explain {topic} in Python")]    
# )
# parser = StrOutputParser()
# chain = prompt|model|parser
# async def main():
#     result = await chain.ainvoke({"topic" : "Decorators"})
#     print(result)
# import asyncio
# asyncio.run(main())

# doubt in  runnable lambda
# import os
# import json
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableLambda
# load_dotenv()
# api_key = os.getenv('GEMINI_API_KEY')
# model = ChatGoogleGenerativeAI(
#     model = 'gemini-3.6-flash',
#     google_api_key = api_key
# )
# prompt = ChatPromptTemplate.from_messages([
#     ("system" , "You are a Python tutor") , 
#     ("human" , "Explain {topic} in Python")]    
# )
# parser = StrOutputParser()
# def clean_text(text):
#     return text.lower()
# cleaner = RunnableLambda(clean_text)
# chain = cleaner|prompt|model|parser
# inputs = ({
#     "topic"  :"Inheritance"
# },
# {
#     "topic" : "Polymorphism"
# }
# )
# result = chain.batch(inputs)
# print(result)

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
model = ChatGoogleGenerativeAI(
    model = 'gemini-3.6-flash',
    google_api_key = api_key
)
prompt = ChatPromptTemplate.from_messages([
    ("system" , "You are a Python tutor") , 
    ("human" , "Explain {topic} in Python")]    
)
parser = StrOutputParser()
chain = RunnableSequence(
    prompt , 
    model , 
    parser
)
for chunk in chain.stream({
    "topic"  : "Inheritance"
}):
    print(chunk , end="")


