from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int
    
new_person: Person = {'name': 'Muneeb Ahmed', 'age': '17'}    
print(new_person)