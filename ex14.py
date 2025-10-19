# Let's have another file that combines the input that we have asked from the user

from sys import argv
import sys

script, user_name = argv

print(f"hello {user_name}. How do you like my script?")
print("Now lets'say I want to ask you several more questions and you need to answer right away??")
age = int(input('>> '))

python_version = sys.version

print(f"So your name is: {user_name} and you are {age} old.")
print("And by the way you are running python version - ", python_version)