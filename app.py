import os
import streamlit as st

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Deepak AI Resume Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #111827 50%, #1e293b 100%);
            color: #f8fafc;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #111827 0%, #0f172a 100%);
            border-right: 1px solid #334155;
        }

        .hero-card {
            padding: 28px;
            border-radius: 22px;
            background: linear-gradient(135deg, #1d4ed8, #7c3aed);
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.30);
            margin-bottom: 24px;
        }

        .hero-title {
            font-size: 42px;
            font-weight: 800;
            margin-bottom: 8px;
            color: white;
        }

        .hero-subtitle {
            font-size: 17px;
            color: #e0e7ff;
        }

        .info-card {
            padding: 18px;
            border-radius: 16px;
            background: rgba(30, 41, 59, 0.85);
            border: 1px solid #334155;
            margin-bottom: 14px;
        }

        .section-heading {
            color: #c4b5fd;
            font-size: 18px;
            font-weight: 700;
        }

        .small-text {
            color: #cbd5e1;
            font-size: 14px;
        }

        .stChatMessage {
            border-radius: 18px;
        }

        div[data-testid="stMetric"] {
            background: rgba(30, 41, 59, 0.80);
            border: 1px solid #334155;
            padding: 12px;
            border-radius: 14px;
        }

        .footer {
            text-align: center;
            color: #94a3b8;
            font-size: 13px;
            margin-top: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# RESUME SECTION DATA
# ============================================================

SUMMARY_TEXT = """PROFESSIONAL SUMMARY

Aspiring Generative AI and AI/ML professional with a foundation in Python,
machine learning, NLP, and data analysis, currently developing skills in
Large Language Models (LLMs), LLM APIs, prompt engineering, embeddings,
LangChain, RAG, vector databases, agentic AI, and AI application development.
Hands-on experience with Python-based AI/ML projects involving data
preprocessing, model development, classification, prediction, and deployment.
Seeking opportunities as a Generative AI Developer, LLM Engineer, AI/ML
Engineer, or Python AI Developer."""


TECHNICAL_SKILLS_TEXT = """TECHNICAL SKILLS

Programming: Python, Object-Oriented Programming (OOP)

Python & Systems: CLI Tools, File Handling, APIs, Logging, Asynchronous
Programming, Multiprocessing, Performance Optimization

NLP & Machine Learning: NLP, Tokenization, Embeddings, Similarity,
Classification, Gradient Descent, Loss Functions, Transformers, Datasets,
Metrics

LLMs & Generative AI: Large Language Models (LLMs), LLM APIs, Chat,
Embeddings, Roles, Function Calling, Safety, Prompt Engineering, Zero-Shot,
Few-Shot, CoT Control, Prompt Templates, Hallucination Control

AI Evaluation & Reliability: Prompt Evaluation

Tools & Collaboration: Git, GitHub, Slack"""


AI_TRAINING_TEXT = """GENERATIVE AI TRAINING

NetSquare Softwares — Generative AI Training | July 2026 – December 2026

Structured training in Generative AI, Large Language Models (LLMs), LLM APIs,
prompt engineering, embeddings, LangChain, RAG, vector databases, agentic AI,
AI evaluation, FastAPI, Streamlit, Gradio, deployment, and AI system design.

Developing practical understanding of LLM applications, orchestration,
retrieval-augmented generation, AI agents, reliability, and AI application
development."""


INTERNSHIP_TEXT = """EXPERIENCE / INTERNSHIPS

ThinkNEXT Technologies Pvt. Ltd. — AI/ML Training | Mohali, Punjab |
June 2025 – July 2025

Completed 45-day Python and AI/ML training focused on Python programming,
data analysis, data preprocessing, machine learning model development,
and practical AI/ML applications.

Worked with machine learning algorithms and real-world datasets, including
preprocessing, model building, evaluation, and deployment concepts.

CGC University Jhanjeri — Python Internship/Training | June 2025 – July 2025

Gained hands-on experience with Python, data preprocessing, and machine
learning model development using real-world datasets.

Used NumPy, Pandas, Matplotlib, and Scikit-learn for data processing,
analysis, visualization, and machine learning workflows."""


PROJECTS_TEXT = """PROJECTS

Movie Recommendation System | Python | Pandas | Scikit-learn | TF-IDF |
Cosine Similarity

Developed a content-based movie recommendation system using Python and a
movie dataset containing movie titles and genres.

Pre-processed and combined movie information into a text representation
for recommendation.

Used TF-IDF (Tfidf-Vectorizer) to convert movie text features into
numerical vectors.

Implemented Cosine Similarity to measure similarity between movies and
generate relevant movie recommendations.

Built recommendation logic that takes a movie title as input and returns
similar movies based on content similarity."""


EDUCATION_TEXT = """EDUCATION

Bachelor of Computer Applications (BCA)
CGC University, Jhanjeri, Punjab | 2023 – 2026 | CGPA: 7.49

Class XII — PSEB
Robin Model Senior Secondary School, Dhuri | 2022 – 2023 | 83%

Class X — PSEB
Robin Model Senior Secondary School, Dhuri | 2021 – 2022 | 89%"""


CERTIFICATION_TEXT = """CERTIFICATIONS

Python — Udemy

30-Day Coding Marathon — CGC University Jhanjeri"""


# ============================================================
# HELPER FUNCTION TO CREATE DOCUMENTS
# ============================================================

def create_section_document(text, section_name):
    return Document(
        page_content=text,
        metadata={
            "section": section_name,
            "source": "Deepak_Garg AI Resume.pdf"
        }
    )


# ============================================================
# LOAD VECTOR STORE
# ============================================================

@st.cache_resource(show_spinner="Loading embedding model and FAISS index...")
def load_vector_store():
    section_docs = [
        create_section_document(SUMMARY_TEXT, "Professional Summary"),
        create_section_document(TECHNICAL_SKILLS_TEXT, "Technical Skills"),
        create_section_document(AI_TRAINING_TEXT, "Generative AI Training"),
        create_section_document(INTERNSHIP_TEXT, "Experience/Internship"),
        create_section_document(PROJECTS_TEXT, "Projects"),
        create_section_document(EDUCATION_TEXT, "Education"),
        create_section_document(CERTIFICATION_TEXT, "Certifications")
    ]

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(
        documents=section_docs,
        embedding=embedding
    )

    return vector_store, len(section_docs)


# ============================================================
# LOAD GEMINI MODEL
# ============================================================

@st.cache_resource
def load_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        temperature=0
    )


# ============================================================
# RAG RESPONSE FUNCTION
# ============================================================

def generate_answer(query, vector_store, llm):

    results = vector_store.similarity_search_with_score(
        query,
        k=3
    )

    # Combine the top 3 retrieved sections
    context_parts = []

    for i, (document, score) in enumerate(results):

        section = document.metadata.get("section", "Unknown")

        context_parts.append(
            f"""
Section: {section}

Content:
{document.page_content}
"""
        )

    context = "\n".join(context_parts)

    prompt = f"""
You are a question-answering assistant for Deepak's resume.

The context below is extracted from Deepak's resume.

Answer the question using only the provided context.

Rules:
1. Give a natural and clear answer.
2. Do not return JSON.
3. Do not invent information.
4. Use the relevant section from the context.
5. If the information is not available, say:
   Information is not available in my database.

Context:
{context}

Question:
{query}

Answer naturally and directly.
"""

    response = llm.invoke(prompt)

    return {
        "answer": response.text,
        "context": context,
        "results": results
    }


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("## 🤖 Deepak AI Assistant")
    st.markdown(
        '<p class="small-text">A Retrieval-Augmented Generation application '
        'powered by FAISS and Gemini.</p>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 👤 Profile")
    st.markdown("**Deepak Garg**")
    st.markdown("Generative AI / AI-ML Developer")
    st.markdown("📍 Punjab, India")

    st.divider()

    st.markdown("### 🧠 Technologies")
    st.markdown(
        """
        - Python
        - LangChain
        - RAG
        - FAISS
        - Hugging Face Embeddings
        - Gemini LLM
        - Streamlit
        """
    )

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">Deepak's AI Resume Assistant 🚀</div>
        <div class="hero-subtitle">
            Ask questions about Deepak's education, skills, training,
            projects, experience, and certifications.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD BACKEND COMPONENTS
# ============================================================

try:
    vector_store, document_count = load_vector_store()
    llm = load_llm()
except Exception as error:
    st.error("Backend initialization failed.")
    st.exception(error)
    st.stop()


# ============================================================
# DASHBOARD METRICS
# ============================================================

metric_1, metric_2, metric_3 = st.columns(3)

with metric_1:
    st.metric("📚 Resume Sections", document_count)

with metric_2:
    st.metric("🔎 Retrieval", "FAISS")

with metric_3:
    st.metric("🧠 LLM", "Gemini")


st.markdown("## 💬 Ask the Resume Assistant")

st.markdown(
    '<p class="small-text">Try asking: '
    '"What are Deepak\'s technical skills?" or '
    '"Tell me about Deepak\'s projects."</p>',
    unsafe_allow_html=True
)


# ============================================================
# CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant" and "details" in message:
            with st.expander("🔍 View retrieval details"):
                details = message["details"]

                st.write("**Retrieved section:**", details["section"])
                st.write("**Source:**", details["source"])
                st.write("**FAISS distance:**", details["score"])

                st.markdown("**Retrieved context:**")
                st.code(details["context"])


# ============================================================
# CHAT INPUT
# ============================================================

query = st.chat_input("Ask something about Deepak's resume...")

if query:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        with st.spinner("Searching resume and generating answer..."):
            try:
                result = generate_answer(
                    query=query,
                    vector_store=vector_store,
                    llm=llm
                )

                answer = result["answer"]

                st.markdown(answer)

                with st.expander("🔍 View retrieval details"):
                    st.write("**Retrieved section:**", result["section"])
                    st.write("**Source:**", result["source"])
                    st.write("**FAISS distance:**", result["score"])

                    st.markdown("**Retrieved context:**")
                    st.code(result["context"])

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "details": result
                    }
                )

            except Exception as error:
                error_message = (
                    "Sorry, an error occurred while generating the answer."
                )

                st.error(error_message)
                st.exception(error)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Built with Python • LangChain • FAISS • Gemini • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
