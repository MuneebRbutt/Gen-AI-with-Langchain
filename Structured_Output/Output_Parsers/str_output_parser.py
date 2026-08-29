from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()

template01 = PromptTemplate(
    template = "Write a brief note on the {topic}",
    input_variables=['topic']
)

template02 = PromptTemplate(
    template = "Write a 5 line summary on the following text. \n {text}",
    input_variables=['text']
)

# Without using str_outputparser
# prompt01 = template01.invoke({'topic': 'the big bang theory'})

# result = model.invoke(prompt01)

# prompt02 = template02.invoke({'text':result.content})

# result01 = model.invoke(prompt02)

# print(result01.content)


# With str_output parser
parser = StrOutputParser()

chain = template01 | model | parser | template02 | model | parser
result = chain.invoke({'topic':'black hole'})

print(result)
