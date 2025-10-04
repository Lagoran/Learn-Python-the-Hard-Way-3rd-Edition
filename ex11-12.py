print("How old are you ?!", end = '\n')
age = input()

print("You are %r years old." % (age))

print(f"So you are {age} years old and that not too bad!")

print("What is you favorite color?")
color = input("Color?:")
print("So you favorite color is: %s" % color)
print(f"So you favorite color is: {color} is it not?".format())

print("Let's combine what we know so far.. ")
print(f"So you are {age} years old and your favorite color is {color}?? You serious???")