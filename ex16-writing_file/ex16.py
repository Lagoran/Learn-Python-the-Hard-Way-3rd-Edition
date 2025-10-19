#let's start with pointing out the file name that we will use

path = "/Users/yordanstrahinov/Documents/GitHub/Learn-Python-the-Hard-Way-3rd-Edition/ex16-writing_file/output.txt"

with open(path) as f2: #mode = 'r' is default so can be skipped as well
    print(f2.read())

print("Now we will write some stuff in this file.")

print("But first let's truncate it!!")

filename = open(path, mode = 'w+')

# print(f"Truncating file {filename} which will actually erase its content")

# filename.truncate()

text1 = str(input("Give me some input text >:"))

filename.write(text1)

filename.close()

f1 = open("./output.txt", mode= 'r+')

print("\nThis is the actual file content:\n",f1.read())

f1.close()