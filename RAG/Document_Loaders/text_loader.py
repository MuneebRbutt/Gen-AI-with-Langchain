from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template = "Generate a summary of the following text:\n\n{text}",
    input_variables = ["text"]
    )
    
loader = TextLoader('football.txt')

docs = loader.load()

# print(type(docs))

print((docs[0]).page_content)

print((docs[1]).metadata)

chain = prompt | model | parser
print(chain.invoke({'text': docs[0].page_content}))







