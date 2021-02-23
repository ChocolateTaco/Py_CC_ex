print("\n10-8 & 10-9. Cats and Dogs Silently")
print("\n==========================")

file1 = '/home/odin/Documents/Python_Zone/Py_CC_ex/Chapter 10/cats.txt'
# try:
#     with open(file1, 'r') as f:
#         catcontents = f.read()
#         print(catcontents)
# except FileNotFoundError:
#     print('File for list of cats is not found')

file2 = '/home/odin/Documents/Python_Zone/Py_CC_ex/Chapter 10/dogs.txt'
# try:
#     with open(file2, 'r') as g:
#         dogcontents = g.read()
#         print(dogcontents)
# except FileNotFoundError:
#     print(f"File {file2} is not found")


def readtext(filepath):
    """Prints out the contents of a file."""
    try:
        with open(filepath, 'r') as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass
        # print(f"The {filepath} cannot be found.") 


paths = [file1, file2]
for i in paths:
    readtext(i)