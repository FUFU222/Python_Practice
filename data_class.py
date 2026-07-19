from dataclasses import dataclass, field
import dataclasses
# class User:
#   def __init__(self, name, age, gender, address, birthday):

#     self.name = name
#     self.age = age
#     self.gender = gender
#     self.address = address
#     self.birthday = birthday

# 上記の書き方をすっきりさせる dataclass↓

# @dataclass
# class User:
#   name: str
#   age: int
#   gender: str
#   address: str
#   birthday: date

# @dataclass
# class User:
#   name: str
#   age: int
#   items: list[int] = field(default_factory=lambda: ['note', 'pen'])

# user = User('supu', 10)
# print(user.name)
# print(user.age)
# print(user.items)

# @dataclass
# class User:
#   name: str
#   age: int

# user = User('toko', 20)
# user.age = 21

# print(user.age)

# class User:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
@dataclass(frozen=True)
class User:
  name: str
  age: int

user = User('supu', 20)
result = dataclasses.asdict(user)

print(user)
print(type(result)) 
print(isinstance(result, dict))