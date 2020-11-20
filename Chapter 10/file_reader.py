# ! currently not working;  should be reading in the file as its in same directory
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# included directory of *.txt file
with open('/home/odin/Documents/Python_Zone/Py_CC_ex/Chapter 10/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

print(contents.rstrip()) # removes line spacing
# rstrip method removes, or strips and white space characters
# from the right side of  a string

