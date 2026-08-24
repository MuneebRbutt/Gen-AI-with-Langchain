from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

messages = [
    HumanMessage(content='Tell me about langchain'),
    SystemMessage(content='You are a helpful assistant')
]

result = model.invoke(messages)

messages.append(AIMessage(content= result.content))
print(messages)
