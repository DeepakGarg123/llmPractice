
import os
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

pdf_path = "Deepak_Garg AI Resume.pdf"
parser = StrOutputParser()
loader = PyPDFLoader(pdf_path)

documents = loader.load()

print("Total pages:", len(documents))

print("\n--- FIRST PAGE METADATA ---")
print(documents[0].metadata)

print("\n--- FIRST PAGE TEXT ---")
print(documents[0].page_content)

summary_text = """PROFESSIONAL SUMMARY 
Aspiring Generative AI and AI/ML professional with a foundation in Python, machine learning, NLP, and data analysis, currently developing skills 
in Large Language Models (LLMs), LLM APIs, prompt engineering, embeddings, LangChain, RAG, vector databases, agentic AI, and AI application 
development. Hands-on experience with Python-based AI/ML projects involving data preprocessing, model development, classification, 
prediction, and deployment. Seeking opportunities as a Generative AI Developer, LLM Engineer, AI/ML Engineer, or Python AI Developer."""

summary_document = Document(
    page_content=summary_text,
    metadata = {
        "section":"Professional Summary",
        "source":"Deepak_Garg AI Resume.pdf"
    }
)
technical_skills_text = """TECHNICAL SKILLS 
Programming: Python, Object-Oriented Programming (OOP) 
Python & Systems: CLI Tools, File Handling, APIs, Logging, Asynchronous Programming, Multiprocessing, Performance Optimization 
NLP & Machine Learning: NLP, Tokenization, Embeddings, Similarity, Classification, Gradient Descent, Loss Functions, Transformers, Datasets, 
Metrics 
LLMs & Generative AI: Large Language Models (LLMs), LLM APIs, Chat, Embeddings, Roles, Function Calling, Safety, Prompt Engineering, Zero-
Shot, Few-Shot, CoT Control, Prompt Templates, Hallucination Control 
AI Evaluation & Reliability: Prompt Evaluation 
Tools & Collaboration: Git, GitHub,  Slack """

technical_skills_document = Document(
    page_content=technical_skills_text,
    metadata = {
        "section":"Technical Skills",
        "source":"Deepak_Garg AI Resume.pdf"
    }
)
AI_training_text = """GENERATIVE AI TRAINING 
NetSquare Softwares — Generative AI Training | July 2026 – December 2026 
• Structured training in Generative AI, Large Language Models (LLMs), LLM APIs, prompt engineering, embeddings, LangChain, RAG, vector 
databases, agentic AI, AI evaluation, FastAPI, Streamlit, Gradio, deployment, and AI system design. 
• Developing practical understanding of LLM applications, orchestration, retrieval-augmented generation, AI agents, reliability, and AI 
application development. """
AI_training_document = Document(
    page_content=AI_training_text , 
    metadata = {
        "section":"Generative AI Training",
        "source":"Deepak_Garg AI Resume.pdf"
    }
)
Internship_text = """EXPERIENCE / INTERNSHIPS 
ThinkNEXT Technologies Pvt. Ltd. — AI/ML Training | Mohali, Punjab | June 2025 – July 2025 
• Completed 45-day Python and AI/ML training focused on Python programming, data analysis, data preprocessing, machine learning model 
development, and practical AI/ML applications. 
• Worked with machine learning algorithms and real-world datasets, including preprocessing, model building, evaluation, and deployment 
concepts. 
CGC University Jhanjeri — Python Internship/Training | June 2025 – July 2025 
• Gained hands-on experience with Python, data preprocessing, and machine learning model development using real-world datasets. 
• Used NumPy, Pandas, Matplotlib, and Scikit-learn for data processing, analysis, visualization, and machine learning workflows. """
Internship_document = Document(
    page_content=Internship_text, 
    metadata = {
        "section":"Experience/Internship",
        "source":"Deepak_Garg AI Resume.pdf"
    }
)
Projects_text = """PROJECTS 
Movie Recommendation System | Python | Pandas | Scikit-learn | TF-IDF | Cosine Similarity 
• Developed a content-based movie recommendation system using Python and a movie dataset containing movie titles and genres. 
• Pre-processed and combined movie information into a text representation for recommendation. 
• Used TF-IDF (Tfidf-Vectorizer) to convert movie text features into numerical vectors. 
• Implemented Cosine Similarity to measure similarity between movies and generate relevant movie recommendations. 
• Built recommendation logic that takes a movie title as input and returns similar movies based on content similarity."""
Projects_document = Document(
    page_content=Projects_text , 
    metadata = {
        "section":"Projects" , 
        "source":"Deepak_Garg AI Resume.pdf"
    }
)
Education_text = """EDUCATION 
Bachelor of Computer Applications (BCA)  CGC University, Jhanjeri, Punjab | 2023 – 2026 | CGPA: 7.49 
Class XII — PSEB  Robin Model Senior Secondary School, Dhuri | 2022 – 2023 | 83% 
Class X — PSEB  Robin Model Senior Secondary School, Dhuri | 2021 – 2022 | 89% """
Education_document = Document(
    page_content=Education_text , 
    metadata = {
        "section":"Education" , 
        "source":"Deepak_Garg AI Resume.pdf"
    }
)
Certification_text = """CERTIFICATIONS 
• Python — Udemy (Link) 
• 30-Day Coding Marathon — CGC University Jhanjeri (Link) 
"""
Certification_document = Document(
    page_content=Certification_text , 
    metadata = {
        "section":"Certification" , 
        "source":"Deepak_Garg AI Resume.pdf"
    }
)

section_docs = [
    summary_document , 
    technical_skills_document , 
    AI_training_document , 
    Internship_document , 
    Projects_document , 
    Education_document , 
    Certification_document 
]
print(len(section_docs))

for i , document in enumerate(section_docs):
    print(f"\n Document{i+1}:")
    print(f"\n Section:" , document.metadata['section'])
    print(f"\n Page_Content:" , document.page_content[:1000])

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)
vector_store = FAISS.from_documents(
    documents=section_docs , 
    embedding = embedding
)
query = "What technical skills do deepak?"

results = vector_store.similarity_search_with_score(
    query,
    k=1
)

retrieved_document = results[0][0]

context = retrieved_document.page_content

prompt = f"""
You are a question-answering assistant for Deepak's resume.

The provided context is extracted from Deepak's resume.
Therefore, information listed in the context belongs to Deepak,
even if his name is not repeated in every section.

Answer the question using the provided context.

If the information is not available, say:
Information is not available in my database.

Context:
{context}

Question:
{query}

Answer naturally and directly.
"""

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.5-flash' , 
    temperature = 0
)
response = model.invoke(prompt)

print(response.text)