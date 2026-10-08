# Delegation tools
import os
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-3.6-flash',
    api_key = os.getenv("GEMINI_API_KEY"),
    temperature = 0
)
# Specialized agents
billing_agent = create_agent(
    model = model,
    tools = [],
    system_prompt=("You are a billing support agent Handle payment,billing,invoice and duplicate charge issues Give a short and helpful response.")
)

technical_agent = create_agent(
    model = model,
    tools = [],
    system_prompt="You are a technical support agent.Handle login problems,application errors, and technical issues.Give a short and helpful response."
)
refund_agent = create_agent(
    model = model,
    tools= [],
    system_prompt="You are refund support agent.Handle cancellation and refund requests.Give a short and helpful response."
)
# Delegate tools
@tool
def delegate_to_billing_agent(request:str)->str:
    """Delegate billing requests to billing agent."""
    result = billing_agent.invoke({
        "messages":[
            {
                "role":"user",
                "content":request
            }
        ]
    })
    return result["messages"][-1].content

@tool
def delegate_to_technical_agent(request:str)->str:
    """Delegate technical requests to technical agent."""
    result = technical_agent.invoke({
        "messages":[
            {
                "role":"user",
                "content":request
            }
        ]
    })
    return result["messages"][-1].content

@tool
def delegate_to_refund_agent(request:str)->str:
    """Delegate refund requests to refund agent."""
    result = refund_agent.invoke({
        "messgaes":[
            {
                "role":"user",
                "content":request
            }
        ]
    })
    return result["messages"][-1].content
# Coordinator agent
coordinator_agent = create_agent(
    model = model,
    tools = [delegate_to_billing_agent , delegate_to_refund_agent , delegate_to_technical_agent],
    system_prompt="You are a coordinator agent for Customer support.Analyze the user's request and decide which specialized.agent should handle it. Use the appropriate delegation tool.Do not solve billing,technical,or refund problems yourself."
)
user_request = input("Enter your request:")
result = coordinator_agent.invoke({
    "messages":[
        {
            "role":"user",
            "content":user_request
        }
    ]
})
print(result["messages"][-1].content)