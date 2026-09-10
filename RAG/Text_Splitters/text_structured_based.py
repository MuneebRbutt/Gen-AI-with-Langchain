# \n \n indicates the paragraph
# \n indicates the line
# "_" indicates the word 
# "" indicates character

# The above guidelines means that the text_structured_based splitter will split the text based on the structure of the text, such as paragraphs, lines, and words. 
# This is useful for documents that have a clear structure, such as academic papers or legal documents.

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separators=["\n\n", "\n", " ", ""]
)

text = """Quaid-e-Azam Muhammad Ali Jinnah was the founder of Pakistan and one of the greatest leaders in the history of the subcontinent. He was born on December 25, 1876, in Karachi. He was a brilliant lawyer, a determined politician, and a strong advocate for the rights of Muslims.

Quaid-e-Azam played a major role in the struggle for a separate homeland for the Muslims of the subcontinent. Under his leadership, the Pakistan Movement gained strength, and after years of political struggle, Pakistan came into existence on August 14, 1947. He became the first Governor-General of Pakistan.

Quaid-e-Azam believed in unity, faith, discipline, equality, and justice. He wanted Pakistan to become a peaceful, democratic, and prosperous country where people could live with freedom and dignity.

He passed away on September 11, 1948. His courage, leadership, and dedication continue to inspire the people of Pakistan. He will always be remembered as the Father of the Nation.

I prefer this response"""

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])