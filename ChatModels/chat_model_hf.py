from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-8B",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

print("Calling model..")

result = model.invoke("Who is the founder of Pakistan?")

print("RESULT:")
print(result)

print("CONTENT:")
print(repr(result.content))