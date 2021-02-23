import json                     # imports json 

filename = 'numbers.json'       # variable for numbers.json
with open(filename) as f:       # opens filename
    numbers = json.load(f)      # json load/read function into numbers variable

print(numbers)              