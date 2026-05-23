'''
TypedDict = rule/blueprint describing what a dictionary should contain

Benifites of using TypedDict 

# Benefit 1 → Autocomplete

- Benefit 1 → Autocomplete
- With TypedDict: vscode suggest valid input parameters 
- This becomes extremely useful in large projects.

Benefit 2 → Prevent Missing Keys

- editor warn about missing key 

inshort TypeDict is describe shape or structure of dictionarly while pydantic validate it . this is why pydantic is most commonly used in real projects

'''

'''
#pydantic 
from pydantic import BaseModel

-> Pydantic is a Python library used to define, validate, parse, and serialize data using Python type hints.
-> Pydantic ensures your data has the correct structure and correct data types at runtime.
This solves the problem that dictionaries and TypedDict do not solve.


# Main Features of Pydantic:

1. Type Validation

2. Automatic Conversion

3. Required Fields

4. Nested Models

Why FastAPI Uses Pydantic?

because it 

Validate
Convert
Generate docs
Return response

'''


from typing import TypedDict


class User(TypedDict):

    name: str
    age: int


user: User = {
    "name" : "Babar",
    # "age"  :  "25",
    "age"  : "twenthy-one"

}

print(f"typedDict output: {user["age"]}")


from pydantic import BaseModel

class User(BaseModel):

    name : str
    reg_no : str
    age : int


user1 = User( 
    name = "Babar raheem",
    reg_no = "22mdbcs241",
    age = 25 )
 

print(f"pydantic output: {user1.age}")


"""
output : typedDict output: twenthy-one
pydantic output: 25

"""
