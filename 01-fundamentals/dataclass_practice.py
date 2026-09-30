from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str

u = User("Neil", 30, "n@x.com")
print (u)
u == User("Neil", 30, "n@x.com")
print (u)
User("Neil", "thirty", "n@x.com")
print (User)