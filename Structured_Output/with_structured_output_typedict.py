from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI()

class Review(TypedDict):
    
    key_points: Annotated[list[str], "Write down the key points of the review, which are worth highlighting."]
    summary: Annotated[str, "A brief summary of the review"]
    sentimant: Annotated[str, "Positive or negative "]
    pros: Annotated[Optional[list[str]], "Write all the pros of this review"]
    cons:  Annotated[Optional[list[str]], "Write all the cons of this review"]
    
structured_model = model.with_structured_output(Review)    

result = structured_model.invoke("The laptops performance is disappointing and it frequently slows down during basic tasks. The battery life is poor and requires frequent charging.The build quality feels cheap considering the price.Overall, I wouldn’t recommend this laptop due to its performance and reliability issues.")
print(result['pros'])
