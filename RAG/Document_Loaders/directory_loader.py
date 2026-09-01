from langchain.community.document_loaders import PyPDFLoader, directory_loader

loader = directory_loader(
    "path",
    glob="**/*.pdf", 
    loader_cls=PyPDFLoader)

