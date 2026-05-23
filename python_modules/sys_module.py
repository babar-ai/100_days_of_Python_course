"""
What is sys in Python?

sys is a built-in Python module that gives you direct access to the Python runtime environment.

In simple words:

sys lets your program talk to Python itself.  


"""



import sys


print(sys.path)         # return list where we can insert 

"""
  return   
  [
 'C:\\Python313\\Lib',
 'C:\\Python313\\DLLs',
 'C:\\MyProject'
]

Think of sys.path as a LIST of folders.

Python uses this list when you write:
import something

It literally does:

👉 Check folder #0
👉 If not found, check folder #1
👉 Then #2
👉 Then #3
…and so on.


sys.path.insert(0, str(Path(__file__).parent))     You told Python: also search my project folder.
"""       