"""#Q1

import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
response  = client.models.generate_content(
    model='gemini-3.6-flash',
    contents='explain what artifical intelligence is in simple words'
)
print(response.text)
"""



"""# Q2

import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
question = input("Write your question:")
response = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=question

)
print(response.text)
"""



"""# Q3
import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
def ask_llm(prompt):
    response = client.models.generate_content(
        model='gemini-3.6-flash',
        contents=prompt
    )
    return response.text
answer  = ask_llm("what is Python? expain me in simple words")
print(answer)
answer1 = ask_llm("what is ai??")
print(answer1)
answer2 = ask_llm("what is machine learning??")
print(answer2)
"""



# Q4.
""""""
# import os
# from dotenv import load_dotenv
# from google import genai
# load_dotenv()
# api_key= os.getenv("GEMINI_API_KEY")
# client = genai.Client(
#     api_key=api_key
# )
# text = input("Enter paragraph:")
# def ask_llm(prompt):
#     response = client.models.generate_content(
#         model='gemini-3.6-flash',
#         contents=prompt
#     )
#     return response.text
# answer = ask_llm(f"""Summarize this paragraph in 2-3 sentences:{text}""")
# print(answer)


# Q5.

# import os
# from dotenv import load_dotenv
# from google import genai
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(
#     api_key=api_key
# )
# text = input("Enter text:")
# Language  = input("Enter language:")
# def ask_llm(prompt):
#     response = client.models.generate_content(
#         model = 'gemini-3.6-flash',
#         contents=prompt
#     )
#     return response.text
# Translation = ask_llm(f"""Translate the following English sentence into {Language}:{text}""")
# print(Translation)
# answer = ask_llm(f"""Translate the following English sentence into {Language}:{text}""")
# print(answer)


# Q6

# import os
# from dotenv import load_dotenv
# from google import genai
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(
#     api_key=api_key
# )
# system_instructions = "You are a Python tutor. Explain programming concepts in simple language and always provide a small example."
# def ask_llm(prompt):
#     response = client.models.generate_content(
#         model='gemini-3.6-flash',
#         contents=prompt,
#         config={
#             "system_instruction":system_instructions
#         }
#     )
#     return response.text
# question1 = ask_llm("What are variables??")
# print(question1)
# question2 = ask_llm("what are loops??")
# print(question2)
# question3 = ask_llm("What are functions??")
# print(question3)


# Q7.
# import os
# from dotenv import load_dotenv
# from google import genai
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(
#     api_key=api_key
# )
# system_instructions = "You are a Python tutor. Explain programming concepts in simple language and always provide a small example."
# def ask_llm(prompt):
#     response = client.models.generate_content(
#         model = 'gemini-3.5-flash',
#         contents=prompt,
#         config={
#             "system_instruction":system_instructions
#         }
#     )
#     return response.text
# code = input("Enter code:")
# code1 = ask_llm(code)
# print(code1)


# Q8.
# import os
# from dotenv import load_dotenv
# from google import genai
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(
#     api_key=api_key
# )
# system_instructions = "You are a Python tutor. Explain programming concepts in simple language and always provide a small example."
# def ask_llm(prompt):
#     try:
#         response = client.models.generate_content(
#             model = 'gemini-2.5-flash' , 
#             contents=prompt,
#             config={
#                 'system_instruction':system_instructions
#             }
#         )
#         return response.text
#     except:
#         return "Unable to connect to the AI service. Please try again."

# question1 = "What are loops??"
# answer = ask_llm(question1)
# print(answer)


# # Q9.

# import os
# from dotenv import load_dotenv
# from google import genai
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)
# def ask_llm(prompt):
#     try:
#         response = client.models.generate_content(
#             model='gemini-3.5-flash',
#             contents=prompt
#         )
#         return response.text
#     except:
#         return "Unable to connect to the AI service. Please try again."    
# while True:
#     question = input("Enter your Question:")
#     if question.lower()=='exit':
#         print("Goodbye")
#         break
#     answer = ask_llm(question)
#     print(answer)


# Q10.

# import os

# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# client = genai.Client(api_key=api_key)


# def ask_llm(prompt):

#     response = client.models.generate_content(
#         model="gemini-3.5-flash",
#         contents=prompt
#     )

#     return response.text


# chat_history = []


# while True:

#     question = input("Ask a question: ")

#     if question.lower() == "exit":
#         print("Goodbye! Have a nice day")
#         break
#     chat_history.append(question)
#     history = "\n".join(chat_history)
#     answer = ask_llm(
#         f"""
# Here are the previous questions asked by the user:

# {history}

# Answer the user's latest question:

# {question}
# """
#     )

#     print("AI:", answer)



# Q11.
# import os
# from dotenv import load_dotenv
# from google import genai
# load_dotenv()
# api_key = os.getenv('GEMINI_API_KEY')
# client = genai.Client(api_key=api_key)
# system_instruction = "You are a professional technical interviewer. Ask the user Python interview questions one at a time.Wait for the answer.Evaluate the answer.Give feedback.Then ask the next question."
# def ask_llm(prompt):
#     response = client.models.generate_content(
#         model = 'gemini-3.5-flash',
#         contents=prompt,
#         config={
#             "system_instruction" : system_instruction
#         }
#     )
#     return response.text
# question = ask_llm("Start the Python Interview by asking the first question. ")
# print(question)
# while True:
#     answer = input("Enter your answer:")
#     if answer.lower()=="exit":
#         print("Goodbye! Have a nice day")
#         break
#     prompt = f"""the candidate's answer:{answer} Evaluate this answer . give feedback out of 10. Then ask the next Python Interview Question."""
#     response = ask_llm(prompt)
#     print(response)



    
# Q12.

# import os
# import time
# from dotenv import load_dotenv
# from google import genai
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# client = genai.Client(api_key=api_key)
# def ask_llm(prompt):
#     for attempt in range(1,4):
#         try:
#             response = client.models.generate_content(
#             model = 'gemini-3.5-flash',
#             contents=prompt
#             )
#             return response.text
        
#         except Exception:
#             print(f"Attempt {attempt} failed. ")
#             if attempt<3:
#                 print("Retrying...")
#                 time.sleep(2)
#     return "Unable to get a response. "
# question = input("Enter Your Question:")
# answer = ask_llm(question)
# print(answer)

# Q13.
import os 
import time
import json
import pandas as pd
from dotenv import load_dotenv
from google import genai
load_dotenv()
sentences_of_history=[]
with open("history.jsonl","r") as file:
    for line in file:
        message=json.loads(line)
        
        sentences_of_history.append(message)
text_history=json.dumps(sentences_of_history)
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
system_instructions = "You are an AI assistant. Answer the user questions in a simple way and polite language."
def ask_llm(prompt):
    for attempt in range (1,4):
        try:
            response = client.models.generate_content(
                model='gemini-3.6-flash',
                contents=prompt,
                config={
                "system_instruction":system_instructions
                }
            )
            return response.text
        except Exception as error :
            print(f"Attempt {attempt} failed")
            if attempt < 3:
                print("Retrying")
                time.sleep(2)
            else:
                return "Unable to get a response"
conversation_history = []
while True:
   question = input("Ask a question:")
   conversation_history.append(question)
   conversation_history.append(text_history)

   if question.lower()=="exit":
      print("Goodbye! Have a nice day")
      break
   answer = ask_llm(conversation_history)
   print(answer)

   with open("history.jsonl","a") as file :
       json.dump(
           {
      "role": "user",
      "content": question
           }
       ,file)
       file.write("\n")
       json.dump(
           {
      "role": "assistant",
      "content": answer
           }
       ,file)
       file.write("\n")
print(ask_llm())
print(sentences_of_history)





        
















                
    





   






