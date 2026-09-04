# Exercise 1: Resume Information Extractor
# ----------------------------------------------------

# Build an AI Resume Information Extractor.

# Input:
# A resume in plain text.

# The LLM must return only structured JSON with:

# {
#   "name": "",
#   "email": "",
#   "phone": "",
#   "location": "",
#   "experience_years": 0,
#   "skills": [],
#   "education": [],
#   "current_role": null
# }

# Requirements:


# Use a reusable prompt template.
# If any information is not available, return null.
# Do not invent missing skills or experience.
# Parse the response into Python.
# Validate all fields using Pydantic.
# Handle invalid JSON/model output.
# Save the validated result into resume_data.json.
# Test the program on at least 5 different resumes.


# import os
# import json
# from pydantic import BaseModel
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")

# client = genai.Client(api_key=api_key)

# resume = """
# Rahul Sharma
# Email: rahul@gmail.com
# Phone: 9876543210
# Location: Delhi

# Python Developer with 3 years of experience.

# Skills:
# Python, Django, PostgreSQL, Git

# Education:
# B.Tech Computer Science
# """

# prompt = f"""
# You are a resume information extraction system.

# Return the information from the resume provided below.

# Return the resume in a valid structured JSON with the below fields:

# {{
#     "name": "",
#     "email": "",
#     "phone": "",
#     "location": "",
#     "experience_years": 0,
#     "skills": [],
#     "education": [],
#     "current_role": null
# }}

# Instructions:

# 1. Extract the information from the resume.
# 2. Do not invent any information.
# 3. If information is not available return null.
# 4. Do not add any extra fields.
# 5. Return only valid JSON.

# Resume:
# {resume}
# """

# response = client.models.generate_content(
#     model="gemini-3.6-flash",
#     contents=prompt
# )

# with open('resume_data.json','w') as file:
#     json.dump(response.text , file , indent=4)







# ====================================================

# Exercise 2: Customer Support Ticket Classifier
# ----------------------------------------------------

# Build an AI system that accepts a customer complaint.

# Example:

# "My internet has been down since yesterday and I have
# already restarted the router twice."

# The output must follow this structure:

# {
#   "category": "",
#   "priority": "",
#   "sentiment": "",
#   "summary": "",
#   "requires_human_support": true
# }

# Allowed categories:


# billing
# technical_support
# account
# delivery
# general


# Allowed priorities:


# low
# medium
# high


# Allowed sentiments:


# positive
# neutral
# negative


# Requirements:


# Use structured output.
# Validate output using Pydantic.
# Prevent values outside the allowed categories.
# Return null if category cannot be determined.
# Process at least 10 customer complaints.
# Count:
# Number of high-priority tickets
# Number of negative tickets
# Tickets requiring human support

# Save all results into tickets.json.


# import os
# import json

# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# client = genai.Client(api_key=api_key)

# complaints = []
# for i in range(10):
#     complaint = input(f"Enter Complaint {i+1}:")
#     complaints.append(complaint)
# prompt = f"""
# You are a customer support ticket classification system.

# Analyze the customer complaint provided below.

# Return only valid JSON with exactly these fields:

# {{
#     "category": "",
#     "priority": "",
#     "sentiment": "",
#     "summary": "",
#     "requires_human_support": true
# }}

# Allowed categories:
# - billing
# - technical_support
# - account
# - delivery
# - general

# Allowed priorities:
# - low
# - medium
# - high

# Allowed sentiments:
# - positive
# - neutral
# - negative

# Instructions:

# 1. Classify the customer complaint.
# 2. Do not invent information.
# 3. Category must be one of the allowed categories.
# 4. Priority must be one of the allowed priorities.
# 5. Sentiment must be one of the allowed sentiments.
# 6. If the category cannot be determined, return null.
# 7. Provide a short summary.
# 8. Return only valid JSON.
# 9. Do not add extra fields.

# Customer complaint:
# {complaints}
# """

# response = client.models.generate_content(
#     model="gemini-3.6-flash",
#     contents=prompt
# )
# print(response.text)

# ====================================================

# Exercise 3: Invoice Data Extraction System
# ----------------------------------------------------

# Create an AI-powered Invoice Parser.

# Input:
# Plain invoice text such as:

# Invoice No: INV-9087
# Customer: ABC Technologies
# Date: 01-09-2026
# Product: Laptop
# Quantity: 3
# Unit Price: 65000
# Tax: 18%

# The LLM must return:

# {
#   "invoice_number": "",
#   "customer": "",
#   "invoice_date": "",
#   "items": [
#     {
#       "product": "",
#       "quantity": 0,
#       "unit_price": 0
#     }
#   ],
#   "tax_percentage": 0,
#   "total_amount": 0
# }

# Requirements:


# Handle multiple invoice items.
# Use nested structured output.
# Validate:
# quantity must be greater than 0
# unit_price cannot be negative
# tax_percentage must be between 0 and 100

# Do not trust the LLM's total blindly.
# Recalculate the invoice total in Python.
# Compare:
#    LLM Total vs Python Calculated Total

# Display a warning if they do not match.
# Save validated invoices into JSON.

import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


invoice = """
Invoice No: INV-9087
Customer: ABC Technologies
Date: 01-09-2026
Product: Laptop
Quantity: 3
Unit Price: 65000
Tax: 18%
"""


prompt = f"""
You are an invoice data extraction system.

Extract the information from the invoice below.

Return only valid JSON with exactly these fields:

{{
    "invoice_number": "",
    "customer": "",
    "invoice_date": "",
    "items": [
        {{
            "product": "",
            "quantity": 0,
            "unit_price": 0
        }}
    ],
    "tax_percentage": 0,
    "total_amount": 0
}}

Instructions:

1. Extract the invoice number.
2. Extract the customer name.
3. Extract the invoice date.
4. Extract all products.
5. Extract quantity and unit price for each product.
6. Extract the tax percentage.
7. Do not invent information.
8. Return only valid JSON.
9. Do not add extra fields.

Invoice:

{invoice}
"""


response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
)
invoice_data = json.loads(response.text)
print(invoice_data)


# ====================================================

# Exercise 4: AI Job Candidate Evaluation Engine
# ----------------------------------------------------

# Inputs:


# Resume
# Job Description


# The AI should return:

# {
#   "candidate_name": "",
#   "matched_skills": [],
#   "missing_skills": [],
#   "experience_years": 0,
#   "required_experience_years": 0,
#   "skill_match_score": 0,
#   "experience_match": true,
#   "recommendation": "",
#   "reason": ""
# }

# Allowed recommendation values:


# shortlist
# review
# reject


# Requirements:


# Do not invent skills that are not present in the resume.
# Match Score must remain between 0 and 100.
# Missing information must return null.
# Validate the result using Pydantic.
# Evaluate at least 5 candidates against the same JD.
# Sort candidates by match score.
# Display the top candidate.
# Save results to candidate_evaluation.json.
# Write a short explanation of why structured output is
#    better than free-form output for this system.



# ====================================================

# Exercise 5: Production-Style Document Intelligence System
# ----------------------------------------------------

# Build a generic AI Document Intelligence application.

# The user provides any text document.

# Possible document types:


# Resume
# Invoice
# Complaint
# Meeting Notes
# Product Description


# The application should first identify the document type.

# Expected first output:

# {
#   "document_type": "",
#   "confidence": 0
# }

# Then, depending on the type, return different structured data.

# Example:

# Resume:
# {
#   "name": "",
#   "skills": [],
#   "experience": 0
# }

# Invoice:
# {
#   "invoice_number": "",
#   "amount": 0
# }

# Complaint:
# {
#   "category": "",
#   "priority": "",
#   "sentiment": ""
# }

# Meeting Notes:
# {
#   "participants": [],
#   "decisions": [],
#   "action_items": []
# }

# Requirements:


# Use separate Pydantic schemas for each document type.
# First classify the document.
# Select the correct schema.
# Extract structured information.
# Validate the output.
# Retry if validation fails.
# Log all validation errors.
# Save valid results to JSON.
# Reject unsupported document types safely.
# Test at least 3 examples for every supported document type.


# BONUS:

# Create the project using:

# main.py
# schemas.py
# llm_service.py
# validator.py
# logger.py
# outputs/

# This exercise should be treated as a mini-project.