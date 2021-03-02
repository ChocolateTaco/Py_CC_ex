print("10-13. Verify User\n=====================")
# The final listing for remember_my.py assumes that either the
##user has already entered their username or that the program is running
##for the first time. We should modify it in case the current user is not the
##person who last used the program.
##Before printing a welcome back message in greet_user(), ask the user if
##that is the correct username. If it's not, call get_a_new_username() to
##get the correct username.

import json, time

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        identity = input(f"Are you {username}? (y or n)\n")
        if identity.lower() == 'y':
            print(f"Welcome back, {username}!")
            time.sleep(2)
        elif identity.lower() == 'n':
            get_new_username()
            time.sleep(2)
        else:
            print('Invalid response was entered, try again.')
            time.sleep(2)
            return None
    else:
        username = get_new_username()
        time.sleep(2)

greet_user()
