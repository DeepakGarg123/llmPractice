import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.messages import HumanMessage , AIMessage
from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    google_api_key = api_key
)
history = InMemoryChatMessageHistory()
prompt = ChatPromptTemplate.from_messages([
    ("system" , "You are a helpful AI Assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human" , "{input}")
])
history = [
    HumanMessage(content="My name is Deepak"),
    AIMessage(content="Nice to meet you Deepak!")
]
result = prompt.invoke({
    "history":history , 
    "input":"What is my name?"
})
response = model.invoke(result)
print(response.text)



import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage , AIMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
model = ChatGoogleGenerativeAI(
    model = 'gemini-3.6-flash',
    google_api_key = api_key
)
prompt = ChatPromptTemplate.from_messages([
    ("system" , "You are a helpful AI Assistant") , 
    MessagesPlaceholder(variable_name="history"),
    ("human" , "{input}")
])
chain = prompt|model
store = {}
def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]
chat_chain = RunnableWithMessageHistory(
    chain , 
    get_session_history ,
    input_messages_key="input" , 
    history_messages_key="history"
)
session_id = "user1"
while True:
    user_input = input("You:")
    if user_input.lower()=="exit":
        break
    response = chat_chain.invoke({
        "input":user_input  
    },
    config={"configurable":{"session_id":session_id}})
    print(response.content)