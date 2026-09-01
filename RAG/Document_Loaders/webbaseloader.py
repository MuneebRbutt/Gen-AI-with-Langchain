from langchain_community.document_loaders import WebBaseLoader

url = "https://priceoye.pk/mobiles/samsung/samsung-galaxy-a07?srsltid=AfmBOopG9OEpVjjuNt7qf90YLdJ373OJ_W5YKFLUVMu-i98zpczZ1DG6"
loader = WebBaseLoader([url])

docs = loader.load()

print(len(docs))

print((docs[0]).page_content)
