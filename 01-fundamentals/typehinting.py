name:str = input("Enter your name: ")
age:str = input ("What's your age?: ")

def greet(name: str, age: int) -> str:
    greet = print(f"Hello, {name}!, age {age}")
    return greet


greet(name, age)