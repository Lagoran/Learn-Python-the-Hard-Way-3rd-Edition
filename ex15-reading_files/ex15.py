from sys import argv

script, filename = argv

txt = open(filename, mode= 'r')

print(f"Here is your textfile: {filename}")
print(txt.read())


print("Type the filename again!! \n")

filename = str(input(">>: "))

print(f"We will read again {filename}!")

filename_again = open(filename, mode = "r+")

print(filename_again.read())