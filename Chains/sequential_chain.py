from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt01 = PromptTemplate(
    template = "Generate a detailed report on the following {topic}.",
    input_variables=['topic']
)

prompt02 = PromptTemplate(
    template = "Generate a five pointer summary from the following text. \n {text}",
    input_variables = ['text'] 
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt01 | model | parser | prompt02 | model | parser

result =chain.invoke({'topic':'Unemployment in Pakistan'})

print(result)

chain.get_graph().print_ascii()