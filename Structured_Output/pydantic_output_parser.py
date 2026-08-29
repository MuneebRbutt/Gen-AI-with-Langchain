from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

class Person(BaseModel):
    
    name : str = Field(description = "Give the name of the person.")
    age : int = Field(gt=18, description="Give the age of the person.")
    city: str = Field(description="Give the city of the person")
 
parser = PydanticOutputParser(pydantic_object=Person)    
template = PromptTemplate(
    template = 'Give the name, age and city of the {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.invoke({'place': 'Pakistan'})

result = model.invoke(prompt)

final_result =parser.parse(result.content)

print(final_result)

    



