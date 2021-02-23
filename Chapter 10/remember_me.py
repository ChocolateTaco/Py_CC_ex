import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)         # reads username.json if exists
    except FileNotFoundError:               
        return None                         # returns None if username.json does not exist
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'              # takes input from user and stores to username.json
    with open(filename, 'w') as f:
        json.dump(username, f)              # reads in the stored username.json to return it
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username          # uses pre-defined function to get username if it exists
    if username:
        print(f"Welcome back, {username}!") # greets user if username.json is populated
    else:
        username = get_new_username         # if username.json doesn't exist, performs pre-defined function of
                                            # get_new_username to create a username
        print(f"We'll remember you when you come back, {username}!")

# get_new_username()
return(username)
greet_user()

