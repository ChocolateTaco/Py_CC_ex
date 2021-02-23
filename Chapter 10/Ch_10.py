print("\n10-8. Cats and Dogs")
print("\n==========================")

file1 = '/home/odin/Documents/Python_Zone/Py_CC_ex/Chapter 10/cats.txt'
try:
    with open(file1, 'r') as f:
        catcontents = f.read()
        print(catcontents)
except FileNotFoundError:
    print('File for list of cats is not found')

file2 = 'dogs.txt'
# file2 = '/home/odin/Documents/Python_Zone/Py_CC_ex/Chapter 10/dogs.txt'
try:
    with open(file2, 'r') as g:
        dogcontents = g.read()
        print(dogcontents)
except FileNotFoundError:
    print(f"File {file2} is not found")