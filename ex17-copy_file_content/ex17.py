from sys import argv
from os.path import exists

script, file1, file2 = argv

file1 = './source_file.txt'

file2 = './destination_file.txt'

source = open(file1)

indata = source.read()

print(f"I am wondering is source file actually exists?? {exists(file1)}")

print(f"the input file is {len(indata)} bytes long..")

print("Then we will copy content over to destination file..")

destination = open(file2, mode = 'w')

print(f"Just wondering if destination exists as well {exists(file2)}")

destination.write(indata)

source.close() # no need to run this line as source file should be already closed after this code: indata = source.read()
destination.close()