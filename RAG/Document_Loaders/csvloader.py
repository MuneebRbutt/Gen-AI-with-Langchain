from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="netflix1.csv", encoding="utf-8")

data = loader.load()

print(data[0])