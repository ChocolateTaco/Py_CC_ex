print('\nCh 6. Dictionaries')
print('=========================')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])     # Telling the program to pring the value of the key, color
print(alien_0['points'])    # Telling the program to pring the value of the key, points


# Removing Key-Value Pairs (using "del" command)
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

print('\nExercise 6.1 Person')
print('=========================')
person = {'First Name' : 'Steve', 'Last Name' : 'Lando', 'Country' : 'United States'}
##print(person)
for i, j in person.items():
    print(i + ' : ' + j)

print('\nExercise 6.2 Favorite Numbers')
print('=========================')
favnums = {'George' : 50, 'Leo' : 26, 'Kobe' : 24, 'Lebron' : 32}
print('The following are favorite numbers of people!')
for i, j in favnums.items():
    print(i + ': ' + str(j))

print('\nExercise 6.3 Glossary')
print('=========================')
vocab = {'Walrus Operator' : 'assigns values to variables as part of a larger expression (Python 3.8)',
         'pass statement' : 'does nothing',
         'break' : 'breaks out of the inntermost enclosing for or while loop',
         'sets' : 'an unordered collection with no duplicate elements',
         '3 quotations' : 'multi-line docstring that can help with documentation',
         'tuples' : 'a list that consists of numbers or values separated by commas'}
print('The following is a glossary of recent python vocabulary words.\n')
for i, j in vocab.items():
    print(i + ': ' + str(j))

print('\n\nLooping Through All Key-Value Pairs')
print('=========================')
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi', }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print('\nExercise 6.4 Glossary Pt2')
print('=========================')
vocab = {'Walrus Operator' : 'assigns values to variables as part of a larger expression (Python 3.8)',
         'pass statement' : 'does nothing',
         'break' : 'breaks out of the inntermost enclosing for or while loop',
         'sets' : 'an unordered collection with no duplicate elements',
         '3 quotations' : 'multi-line docstring that can help with documentation',
         'tuples' : 'a list that consists of numbers or values separated by commas',
         'sorted' : 'returns a new sorted list in simple ascending order',
         'range' : 'generates values within a given range',
         'defintion' : 'keyword def that precurses a function definition',
         'list' : 'number of compound data types grouped together',
         'while loop' : 'executes a condition as long as it is met'}
print('The following is a glossary of recent python vocabulary words.\n',)
for i, j in vocab.items():
    print(i + ': ' + str(j))


print('\nExercise 6.5 Rivers')
print('=========================')
rivers = {'nile' : 'egypt', 'amazon' : 'south america', 'yangtze' : 'china'}
for riv, loc in rivers.items():     # don't forget the _.items(), otherwise _.keys; _.values
    print(f"{riv.title()} is located in the infamous {loc.title()}!")
    print(f"{riv.title()} is a very large river.")
    print(f"{loc.title()} is a country, or so I think?")


print('\nExercise 6.6 Polling')
print('=========================')
favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
registers = ['jen', 'sarah', 'leon', 'james']
##for name, language in favorite_languages.items():
##	print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    if name in registers:
        print(f"Hey {name.title()}, thank you for taking the poll.")
    else:
        print(f"Hey {name.title()}, best on hurry up and take the poll.")


print('\nExercise 6.7 People')
print('=========================')
person1 = {'First Name' : 'Steve', 'Last Name' : 'Lando', 'Country' : 'United States'}
##print(person)
##for i, j in person1.items():
##    print(i + ' : ' + j)
person2 = {'First Name' : 'John', 'Last Name' : 'Doe', 'Country' : 'England'}
person3 = {'First Name' : 'Mario', 'Last Name' : 'Cabinari', 'Country' : 'Italy'}
people = [person1, person2, person3]
##print(people)
for i in people:
    print(i)
    
print('\nExercise 6.8 Pets')
print('=========================')
pet1 = {'Type' : 'dog', 'Owner' : 'Ronald'}
pet2 = {'Type' : 'cat', 'Owner' : 'Jackie'}
pet3 = {'Type' : 'hamster', 'Owner' : 'Antoinette'}
pets = [pet1, pet2, pet3]

for animal in pets:
    print(animal['Owner'] + " has a pet " + animal['Type'])


print('\nExercise 6.9 Favorite Places')
print('=========================')
favorite_places = {'Bob' : ['Italy', 'London', 'Paris'], 'Anna' : ['Chicago', 'Los Angeles'],
                   'Reggie' : ['China', 'Vietnam', 'Japan']}


for name, placeS in favorite_places.items():
    print(f"{name.title()}'s favorite places to visit are:")
    for place in placeS:
        print(f"\t{place.title()}")



print('\nExercise 6.10 Favorite Numbers Part 2')
print('=========================')
favnums = {'George' : [50, 23], 'Leo' : [26, 99, 69, 1], 'Kobe' : [8, 24], 'Lebron' : [32]}
print('The following are favorite numbers of people!')
for i, j in favnums.items():
    if len(j) < 2:                          # Only works for lists or strings, would not work for integers
        print(f"{i.title()}'s favorite number is: ")
        for p in j:
            print(f"\t" + str(p))
    elif len(j) >  1:
        print(f"{i.title()}'s favorite numbers are: ")
        for p in j:
            print(f"\t" + str(p))
    

print('\nExercise 6.11 Cities')
print('=========================')
# Creating a dictionary that includes holds a set of dictionaries (keys with multipple values)
cities = {'Mumbai' :
          {'Country' : 'India',
           'Population' : 12478447,
           'Fact' : 'World’s most expensive house is in Mumbai'},
          'Los Angeles' :
          {'Country' : 'United States of America',
           'Population' : 3979576,
           'Fact' : 'Home of Hollywood movies'},
          'Dubai' :
          {'Country' : 'United Arab Emirates',
           'Population' : 3390000,
           'Fact' : 'Business hub of Western Asia'}
          }

# Challenging step
for city, data in cities.items():       # Calling the two values from the cities' dictionaries
    print(f"City: {city.title()}")      # Print the title of the first value and capitalize it
    coun = f"{data['Country']}"         # Recalling the 'Country' key from the "data" dictionary within Cities
    pop = f"{data['Population']}"       # Recalling the 'Population' key from the "data" dictionary within Cities
    faq = f"{data['Fact']}"             # Recalling the 'Fact' key from the "data" dictionary within Cities

    print(f"\tCountry: {coun.title()}") # Print tab with a label, followed by the previous recall of coun
    print(f"\tPopulation: {pop}")       # Print tab with a label, followed by the previous recall of pop
    print(f"\tFact: {faq.title()}\n")   # Print tab with a label, followed by the previous recall of faq
