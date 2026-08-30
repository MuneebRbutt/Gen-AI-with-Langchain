from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

parser = StrOutputParser()

class Feedback(BaseModel):
    
    sentiment: Literal['positive', 'negative'] = Field(description="Classify the sentiment of the feedback.")

parser02 = PydanticOutputParser(pydantic_object=Feedback)

model = ChatOpenAI()

prompt01 = PromptTemplate(
    template='Give the sentiment of the following feedback. \n {feedback}.\n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser02.get_format_instructions()}
    
)

prompt02 = PromptTemplate(
    template = 'Give a professional and appropriate response to this positive feedback.\n {feedback}',
    input_variables = ['feedback']
)

prompt03 = PromptTemplate(
    template = 'Give a professional and appropriate response to this negative feedback.\n {feedback}',
    input_variables=['feedback']
)

branch_chain =RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt02 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt03 | model | parser),
    (RunnableLambda(lambda x: 'Could not found sentiment'))
)


classifier_chain = prompt01 | model | parser02

# result = (classifier_chain.invoke({'feedback':'This is an outdated and terrible phone'}))
# print(result.sentiment)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': 'This is a terrible phone with a terrible battery time'})

# print(result)

chain.get_graph().print_ascii()