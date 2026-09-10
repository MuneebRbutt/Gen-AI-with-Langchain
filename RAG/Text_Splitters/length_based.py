from langchain_text_splitters import CharacterTextSplitter 
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader("Business.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)

chunks = splitter.split_documents(docs)

print(chunks[0])
