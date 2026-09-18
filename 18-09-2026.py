from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
sentences_1 = ["Hello my name is Deepak!"]
sentences_2 = "Deepak analysing the weather"
sentences_3 = "Deepak is speaking to the karan about weather"
embedding_1 = model.encode(sentences_1)
embedding_2 = model.encode(sentences_2)
embedding_3 = model.encode(sentences_3)
similarity = cosine_similarity(embedding_1 , [embedding_2 , embedding_3])
print(similarity)






from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
text = "Artifical Intelligence can be a boon or curse for human beings."
vector = embedding.embed_query(text)
print(vector)


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
text = """
Python is a programming language.Python is easy to learn.Python is used in artificial intelligence.Python is used in machine learning.Python has many useful libraries.
"""
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 80 , 
    chunk_overlap = 10
)
chunks = splitter.split_text(text)
embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
vectors = embedding.embed_documents(chunks)
connecting = list(zip(chunks ,vectors))
vector_store = FAISS.from_embeddings(
    text_embeddings = connecting , 
    embedding=embedding
)
result = vector_store.similarity_search_with_score(
    "How is Python used in AI?" , 
    k=2
)
print(result)




