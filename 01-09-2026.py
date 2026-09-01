# Exercise 15 — :rocket: Production-Style AI Assistant
# Build a complete AI Developer Assistant CLI.
# The assistant should be able to:
# 1. Answer questions
# You: Explain Python decorators.
# 2. Explain code
# You: /explain
# Then allow the user to enter Python code.
# 3. Generate code
# You: /code
# Example:
# Create a Python function to check whether a number is prime.
# 4. Summarize text
# You: /summarize
# 5. Maintain conversation
# The assistant should remember the current conversation.
# 6. Save conversation
# When the user exits:
# conversation.json
# 7. Error handling
# Handle API failures gracefully.
# 8. Retry
# Retry failed requests up to 3 times.
# 9. Logging
# Create:
# app.log
# Log:

# Application started
# User request received
# API request started
# API request completed
# API error
# Retry attempt
# Application closed
# 10. Environment variables
# The API key must come from an environment variable.
# Do NOT hard-code the API key in the Python file.
# Expected architecture
# AI Developer Assistant
# │
# ├── main.py
# ├── llm.py
# ├── config.py
# ├── logger.py
# ├── conversation.py
# ├── conversation.json
# ├── app.log
# ├── .env
# └── .gitignore
# Bonus
# Add:
# /model
# to allow the user to select/configure the model.
# Add:
# /history
# to display previous conversation messages.
# Add:
# /clear
# to clear the current conversation.


import os
import time
import json
import logging

from dotenv import load_dotenv
from google import genai


load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


conversation = []



def ask_llm(prompt):
    for attempt in range(1,4):
        try:
            logging.info("API request started.")

            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )
            logging.info("API request completed")

            return response.text
        except Exception as e:
            print(f"Attempt {attempt} failed :{e} ")
            if attempt<3:
                logging.info(f"Retry attempt :{e}")
                print("Retrying...")
                time.sleep(2)
    return "Unable to get a response. "
            
            

while True:

    question = input("You: ")

    
    if question.lower() == "exit":

        with open("conversation.json", "w") as file:
            json.dump(conversation, file, indent=4)

        print("Conversation saved to conversation.json")
        print("Goodbye! Have a nice day.")

        break

    
    if question.lower() == "explain":

        code = input("Enter Python Code:")

        prompt = f"""
Explain the following Python code in simple words for beginners.

It should include:

1. Definitions
2. Real-life examples
3. One more practice question

Code:
{code}
"""

        answer = ask_llm(prompt)

        print("AI:", answer)

        continue

    
    if question.lower() == "code":

        request = input("What code should I generate:\n")

        prompt = f"""
Generate Python code for the following requirement.

Requirement:
{request}

Please include:

1. Clean Python code
2. Explanation in simple words
3. One practice question
"""

        answer = ask_llm(prompt)

        print("AI:", answer)

        continue

    
    if question.lower() == "/summarize":

        text = input("Enter text to summarize:\n")

        prompt = f"""
Summarize the following text in simple words for beginners.

Text:
{text}

Please include:

1. Short summary
2. Main points
3. Easy explanation
"""

        answer = ask_llm(prompt)

        print("AI:", answer)

        continue
    conversation.append({
        "role": "user",
        "content": question
    })
    prompt = f"""
Here is the conversation so far:

{conversation}

Answer the user's latest question naturally.
"""

    answer = ask_llm(prompt)

    print("AI:", answer)

    conversation.append({
        "role": "assistant",
        "content": answer
    })

    

    

    

    



