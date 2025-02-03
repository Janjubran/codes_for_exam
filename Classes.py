from dataclasses import dataclass
@dataclass
class stu:
    name: str
    age: int
    id: int
    Major: str = 'CS'

student3 = stu('chris',5,3234234)
print(student3.id)
