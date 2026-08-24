from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
chat_history = [
    SystemMessage(content='You are an helpful AI assistant')
]

while True:
    user_input = input("You:")
    chat_history.append(HumanMessage(content = 'user_input'))
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    result = model.invoke(AIMessage(content='chat_history'))
    chat_history.append(result.content)
    print("Chatbot:", result.content)