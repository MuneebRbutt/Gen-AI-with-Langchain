from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model_name="gpt-4")

result =model.invoke("What is the definition of computer?")

print(result.content)
