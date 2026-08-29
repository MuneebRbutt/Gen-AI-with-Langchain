from pydantic import BaseModel, Field
from typing import Literal, Optional 
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
class Review(BaseModel):
    
    key_points: list[str] = Field("Write down the key points of the review, which are worth highlighting.")
    summary: list[str] = Field(description="A brief description of the review")
    sentimant: Literal['positive', 'negative', 'neutral'] = Field(description ="Return sentimant of the review, positive, negative or neutral")
    pros: Optional[list[str]] = Field(default = None, description= "Write the pros of the review")
    cons: Optional[list[str]] = Field(default = None, description= "Write the cons of the review")
    
structured_model = model.with_structured_output(Review)    

result = structured_model.invoke("The laptops performance is disappointing and it frequently slows down during basic tasks. The battery life is poor and requires frequent charging.The build quality feels cheap considering the price.Overall, I wouldn’t recommend this laptop due to its performance and reliability issues.")
print(result.sentimant)
    
        