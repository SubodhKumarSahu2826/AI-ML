from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person={'name': 'Subodh Kumar Sahu', 'age': 21}
print(new_person)