from sys import argv
import sys

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print("Let me print the python version for you:", sys.version)
print("Let me also print the sys argv for you:", sys.argv)
print("Let's print the current path of this python file:", sys.path)