"""
What is a Regular Expression (Regex)?

👉 A regular expression (regex) is a pattern used to search, match, or extract text.

🔍 Simple Meaning

👉 Think of regex as:

A smart text search tool with rules   


"""

import re

text = "batch12"
match = re.search(r"\d+", text)

print(match.group())


# example 2               r"\w+@\w+\.\w+"        email patteren



