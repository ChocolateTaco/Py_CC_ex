import json                     # imports json (JSON = Javascript Object Notation)

numbers = [2,3,5,7,11,13]       # list of numbers to start with

filename = 'numbers.json'       # name a *.json file
with open(filename, 'w') as f:  # opens the json file
    json.dump(numbers, f)       # stores the numbers as a json file
