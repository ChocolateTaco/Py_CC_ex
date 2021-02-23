print("10-11. Favorite Number\n=====================")
# Write a program that prompts for the user's favorite number. Use json.dump()
# to store this number in a file. Write a separate program that reads in this
# value and prints the message, "I know your favorite number! It's _____."

import json

def ask_fav_num():
    """Asks the user for a favorite number and spits it out"""
    filename = 'favenum.json'
    with open(filename, 'w') as f:
        fav = input("What's your favorite number?\n")
        json.dump(fav, f)
        f.close()
        print("Got your favorite number saved.")

    
def read_fav_num():
    """Reads in the favorite number if it exists."""
    filename = 'favenum.json'
    try:
        with open(filename, 'r') as f:
            favnum = json.load(f)
            print("I know your favorite number! It's " + favnum)
    except FileNotFoundError:
        print("Sorry your favorite number has yet to been saved.")
        
ask_fav_num()
read_fav_num()


