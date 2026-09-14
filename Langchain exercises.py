# ====================================================
# Exercise 1: Basic RunnableSequence
# ====================================================

# Create a LangChain pipeline using:

# Prompt Template
#     ↓
# LLM
#     ↓
# StrOutputParser

# Input:
# topic = "Python generators"

# The model should explain:
# - Definition
# - Simple example
# - One real-world use case

# Requirements:
# 1. Use ChatPromptTemplate.
# 2. Use LCEL with the | operator.
# 3. Execute using invoke().
# 4. Print only the final parsed string.
"""
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an experienced {role}."),
    ("human", "Explain {topic}")
])
parser = StrOutputParser()
chain = prompt | model | parser

result = chain.invoke({
    "role": "Python Trainer",
    "topic": "decorators"
})
print(result)
"""
# ====================================================
# Exercise 2: Dynamic Learning Assistant
# ====================================================

# Create a reusable chain that accepts:

# {
#     "topic": "",
#     "level": ""
# }

# Example:

# topic = "Machine Learning"
# level = "beginner"

# The response should include:
# - Simple explanation
# - Example
# - 3 key points
# - 2 questions for practice

# Requirements:
# 1. Do not hard-code the topic.
# 2. Use ChatPromptTemplate.
# 3. Use model + StrOutputParser.
# 4. Test the same chain with at least 4 different topics.
"""
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
model = ChatGoogleGenerativeAI(
    model = 'gemini-3.6-flash',
    google_api_key = api_key
)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an experienced {role}."),
    ("human", "Explain {topic}")
])
parser = StrOutputParser()
chain = prompt|model|parser
inputs = [
    {"role": "Python developer" , "topic":"functions"},
    {"role": "Java developer" , "topic":"decorators"},
    {"role": "Data analyst" , "topic" : "insights"}
]
result = chain.batch(inputs)
print(result)
"""

# ====================================================
# Exercise 3: RunnableLambda Preprocessing
# ====================================================

# Create a LangChain pipeline where user input is cleaned before
# being sent to the LLM.

# Input example:

# "     EXPLAIN   RECURSION IN PYTHON     "

# Create a Python function that:
# - Removes leading/trailing spaces.
# - Normalizes unnecessary spaces.

# Convert the function into RunnableLambda.

# Pipeline:

# Raw Input
#     ↓
# RunnableLambda
#     ↓
# Prompt
#     ↓
# LLM
#     ↓
# Parser

# Requirements:
# 1. Use RunnableLambda.
# 2. Do not clean the input outside the chain.
# 3. Print the cleaned input and final response.


import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
model = ChatGoogleGenerativeAI(
    model = 'gemini-3.6-flash',
    google_api_key = api_key
)
prompt = ChatPromptTemplate.from_messages([
    ("system" , "You are an experienced Python developer."),
    ("human" , "Explain {topic}")
])
def clean_text(text):
    text = text.strip()
    text = " ".join(text.split())
    return text
cleaner = RunnableLambda(clean_text)
parser = StrOutputParser()
chain = cleaner|prompt|model|parser
input = "Explain Python functions. "
result = chain.invoke(input)
print(result)

# ====================================================
# Exercise 4: Batch Processing
# ====================================================

# Create a chain that explains technical concepts.

# Process these topics using batch():

# - REST API
# - Docker
# - Git Rebase
# - SQL Index
# - Async Programming

# For each topic generate:
# - Definition
# - One example
# - One interview question

# Requirements:
# 1. Use only one reusable chain.
# 2. Use batch(), not a manual invoke() for every topic.
# 3. Store all outputs in a list.
# 4. Print outputs with the corresponding topic names.



# ====================================================
# Exercise 5: Streaming AI Tutor
# ====================================================

# Build an AI tutor where the response appears progressively
# instead of waiting for the complete output.

# User should enter:

# Example:

# Topic: Neural Networks
# Difficulty: Intermediate

# Requirements:
# 1. Use ChatPromptTemplate.
# 2. Use LCEL.
# 3. Use stream().
# 4. Print each returned chunk immediately.
# 5. Add an "exit" command to stop the application.

# Expected behavior:

# AI: Neural
# AI: networks
# AI: are
# AI: ...

# The user should see the response appear gradually.



# ====================================================
# Exercise 6: Sequential Content Pipeline
# ====================================================

# Create a multi-stage pipeline.

# Input:
# A technical topic.

# Example:

# "Vector Databases"

# Stage 1:
# Generate a detailed explanation.

# Stage 2:
# Take the explanation and generate a short summary.

# Stage 3:
# Take the summary and generate 5 interview questions.

# Flow:

# Topic
#    ↓
# Explanation Chain
#    ↓
# Summary Chain
#    ↓
# Interview Question Chain

# Requirements:
# 1. Create separate prompts for every stage.
# 2. Output from one stage must become input to the next stage.
# 3. Use LangChain runnables/LCEL.
# 4. Print:
#    - Full explanation
#    - Summary
#    - Interview questions



# ====================================================
# Exercise 7: RunnableParallel — Article Analyzer
# ====================================================

# Input:
# A long article or paragraph.

# Analyze the same input simultaneously for:

# 1. Summary
# 2. Sentiment
# 3. Keywords
# 4. Suggested title

# Architecture:

#                 ARTICLE
#                    ↓
#            RunnableParallel
#         ┌──────────┼──────────┐
#         ↓          ↓          ↓
#      Summary   Sentiment   Keywords
#                     ↓
#                   Title

# Requirements:
# 1. Create separate chains for each task.
# 2. Combine them using RunnableParallel.
# 3. Return one Python dictionary.

# Expected output:

# {
#     "summary": "...",
#     "sentiment": "...",
#     "keywords": "...",
#     "title": "..."
# }

# 4. Print each field separately.



# ====================================================
# Exercise 8: Parallel + Sequential Combined Pipeline
# ====================================================

# Build a Product Review Intelligence System.

# Input:

# "The headphones sound excellent but the battery only lasts
# three hours and they are expensive."

# First run these tasks in parallel:

# - Sentiment analysis
# - Problem extraction
# - Positive feature extraction

# Then use all three outputs to generate:

# - Final customer support recommendation

# Architecture:

#                     REVIEW
#                       ↓
#                RunnableParallel
#              /        |        \
#             ↓         ↓         ↓
#        Sentiment   Problems   Positives
#              \        |        /
#                   Combined
#                       ↓
#               Recommendation LLM
#                       ↓
#                 Final Response

# Requirements:
# 1. Use RunnableParallel.
# 2. Create a second chain after the parallel stage.
# 3. Feed parallel results into the recommendation prompt.
# 4. Do not manually copy each generated answer into another prompt.



# ====================================================
# Exercise 9: RunnablePassthrough — Question Analysis
# ====================================================

# Create an application where the original user question must be
# preserved while additional information is generated.

# Input:

# "Why is caching useful in web applications?"

# Pipeline should generate:

# Original Question
#       ↓
#  ┌───────────────┐
#  ↓               ↓
# Keep Question   Generate Key Concepts
#  ↓               ↓
#  └───────┬───────┘
#          ↓
#       Final Prompt
#          ↓
#         LLM

# Use RunnablePassthrough so that the original question remains
# available later in the chain.

# Final answer must include:
# - Original question
# - Explanation
# - Important concepts
# - One practical example

# Requirements:
# 1. Use RunnablePassthrough.
# 2. Do not manually store/reinsert the original question after
#    the pipeline begins.
# 3. Explain in comments why RunnablePassthrough was useful.



# ====================================================
# Exercise 10: Advanced AI Research Report Pipeline
# ====================================================

# Build a complete LangChain application that accepts a technical
# topic such as:

# "Agentic AI"
# "RAG"
# "Microservices"
# "Cloud Computing"

# The system should perform:

# STEP 1:
# Generate an initial explanation.

# STEP 2:
# Run these analyses in parallel:

# - Key concepts
# - Benefits
# - Limitations
# - Real-world applications
# - Interview questions

# STEP 3:
# Use all generated outputs to create one final structured report.

# Expected structure:

# {
#     "topic": "...",
#     "overview": "...",
#     "key_concepts": [...],
#     "benefits": [...],
#     "limitations": [...],
#     "applications": [...],
#     "interview_questions": [...]
# }

# Architecture:

#                       TOPIC
#                         ↓
#                 Explanation Chain
#                         ↓
#                 RunnableParallel
#          ┌────────┬─────┼─────┬────────┐
#          ↓        ↓     ↓     ↓        ↓
#       Concepts Benefits Risks Uses Questions
#          └────────┴─────┼─────┴────────┘
#                         ↓
#                   Final Report Chain
#                         ↓
#                  Structured Result

# Requirements:
# 1. Use ChatPromptTemplate.
# 2. Use multiple reusable chains.
# 3. Use RunnableParallel.
# 4. Use RunnablePassthrough where appropriate.
# 5. Use RunnableLambda for at least one preprocessing or
#    postprocessing operation.
# 6. Use invoke() for the main execution.
# 7. Add a streaming option for the final report.
# 8. Handle exceptions properly.
# 9. Keep the API key in .env.
# 10. Organize project into multiple Python files.