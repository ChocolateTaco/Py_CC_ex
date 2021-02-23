def thewordcount(filepath):
    """This function counts all instances of "the " in a txt file."""
    try:
        with open(filepath, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
            print(f"Sorry, {filepath} cannot be found.")
    else:
        # words = contents.split()
        print(contents.lower().count('the '))   # prints out number of lower cased "the " there are


thewordcount("/home/odin/Documents/Python_Zone/Py_CC_ex/Chapter 10/The Yellow Wallpaper.txt")