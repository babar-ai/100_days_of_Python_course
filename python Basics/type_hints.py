

''''
type_hints:
        allows developers to specify the expected data types of variables, function arguments, and return values. While Python is dynamically typed, 
        type hints improve code readability, help catch errors early during development, and enable better tooling support.


'''

# Syntax of Type Hints / Type Annotations

name: str = 'Babar'
Reg_no: int = 241

def greet(name: str) -> str:
    return f'hello, {name}'

# Optional Type
'''
Use Optional when a value can be of a specified type or None:
'''
from typing import Optional

#funtion Annotation
def find_user(user_id: int) -> Optional[str]:
    
    if user_id == 0:
        return None
    
    return 'User Name'

#some more advance type_hints or type Annotation
#List
from typing import List, Dict, Set, Any
x: List[List[int]] = [[1,2,3],[]]

#Dictionary 
x: Dict[str, str] = {"a":"b"}
x: Set[str] = {'a','b'}

# WE can also do this like
Vector = Dict[str, str] 

def foo(d: Vector) -> Vector:
    print(d)
    

#Any
def foo(output: Any):
    pass

'''
1. What is Union?

Union means:

A variable can accept multiple possible data types.

'''

# from typing import Union

# Reg_No : Union[int, str]
Reg_No : int | str

# we can also write 

Reg_No = "22MDBCS241"

print(f'my registration no is {Reg_No}')



'''
Literal means:

Variable can only contain specific exact values.

Note: even if we pass anther value that is not define in literal still it will execute . why?

Because Python itself does NOT enforce type hints at runtime.

to achevie run time validation then use "Pydantic library"
same case goes for all type hints

'''

from typing import Literal

status: Literal['INPROGRESS', 'COMPLETETED', 'PENDING']

status = 'INPROGRES'

# print(f'my status is {status}')

#example 2

def set_theme(
    mode: Literal["dark", "light"]
):
    print(mode)


set_theme(mode="day")



'''
#Annotated

In Python, Annotated is a type hint introduced in Python 3.9+ (via the typing module) that lets you attach extra
 metadata to a type. The metadata doesn't change how the type works in Python itself, but libraries and frameworks
can use it for validation, documentation, or other purposes.

'''

from typing import Annotated

age: Annotated[int, "Must be between 18 and 100"] = 25


'''


'''