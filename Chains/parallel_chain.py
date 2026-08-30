from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model01 = ChatOpenAI()

model02 = ChatOpenAI()

prompt01 = PromptTemplate(
    template = "Generate short and simple notes from the following {text}",
    input_variables=['text']
)

prompt02 = PromptTemplate(
    template = "Generate five short questions from the following. \n {text}",
    input_variables=['text']
)

prompt03 = PromptTemplate(
    template = "Merge the notes and quizzes into a single document \n notes->{notes} quiz->{quiz}",
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt01 | model01 | parser,
    'quiz' : prompt02 | model02 | parser   
})
                                  
merge_chain = prompt03 | model01 | parser    

chain = parallel_chain | merge_chain

text = """
A decision tree is a non-parametric supervised learning algorithm, which is utilized for both classification and regression tasks. It has a hierarchical, tree structure, which consists of a root node, branches, internal nodes and leaf nodes.

As you can see from the diagram below, a decision tree starts with a root node, which does not have any incoming branches. The outgoing branches from the root node then feed into the internal nodes, also known as decision nodes. Based on the available features, both node types conduct evaluations to form homogenous subsets, which are denoted by leaf nodes, or terminal nodes. The leaf nodes represent all the possible outcomes within the dataset.

"""


result =chain.invoke({'text': text}) 
# print(result)   

chain.get_graph().print_ascii()                          
    




