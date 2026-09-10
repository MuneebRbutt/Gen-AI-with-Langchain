from langchain_text_splitters import RecursiveCharacterTextSplitter, Language


text = """class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def passed(self):
        return self.average() >= 50


def display_result(student):
    print(f"Student: {student.name}")
    print(f"Average: {student.average()}")

    if student.passed():
        print("Result: Passed")
    else:
        print("Result: Failed")


students = [
    Student("Ali", [70, 80, 90]),
    Student("Sara", [45, 50, 40]),
    Student("Ahmed", [88, 92, 85])
]

for student in students:
    display_result(student)
    print("-" * 20)
"""


splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=350,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])

