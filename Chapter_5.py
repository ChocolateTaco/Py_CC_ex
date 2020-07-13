##print('\n5-1. Conditional Tests')
##car = 'subaru'
##
##print("Is car == 'subaru'? I predict True.") 
##if car == 'subaru':
##	print("car == subaru")
##
##print("\nIs car == 'audi'? I predict False.") 
##if car == 'audi':
##	print("car == audi")
##
##print('\n5-2. More Conditional Tests')
##print('Enter a string')
##string1 = input()
##string2 = 'gooble gobble'
##string1 in string2
##len(string1) == len(string2)
##
##
##groceries = ['tomatoes', 'potatoes', 'lemon', 'milk', 'eggs']
##'taco shell' in groceries

print('\n5-3. Alien Color #1, #2')
print('=========================')
alien_color = 'red'
if alien_color == 'green':
    print("You've just earned 5 points!")
elif alien_color != 'green':
    print("You've just earned 10 points!")
else:
    print("You've just earned 10 points!")

##################################
print('\n5-5. Alien Colors #3')
print('=========================')
alien_color = 'green' # Green version
if alien_color == 'green':
    print("You've just earned 5 points for shooting the green alien!")
elif alien_color == 'yellow':
    print("You've just earned 10 points for shooting the yellow alien!")
else:
    print("You've just earned 15 points shooting the red alien!")

alien_color = 'yellow' # Yellow version
if alien_color == 'green':
    print("You've just earned 5 points for shooting the green alien!")
elif alien_color == 'yellow':
    print("You've just earned 10 points for shooting the yellow alien!")
else:
    print("You've just earned 15 points shooting the red alien!")

alien_color = 'red' # Red version
if alien_color == 'green':
    print("You've just earned 5 points for shooting the green alien!")
elif alien_color == 'yellow':
    print("You've just earned 10 points for shooting the yellow alien!")
else:
    print("You've just earned 15 points shooting the red alien!")


##################################
##print('\n5-6. Stages of Life')
##print('=========================')
##print('Enter your age')
##age = input()
##if int(age) < 2:
##    print('Ah look at the baby!')
##elif int(age) == 2 or int(age) < 4:
##    print('A toddler, all potty trained now?')
##elif int(age) == 4 or int(age) < 13:
##    print('A kid eh?')
##elif int(age) == 13 or int(age) < 20:
##    print('A teenager!?')
##elif int(age) == 20 or int(age) < 65:
##    print('An adult, watch out for them responsibilities!')
##elif int(age) >= 65:
##    print('Hello Elder One.')


##################################
print('\n5-7. Favorite Fruit')
print('=========================')
fruits = ['tomatoes', 'apple', 'lemon', 'pineapple', 'strawberries']
if 'bananas' in fruits:
    print("It's bananas! B-A-N-A-N-A-S!")
if 'apples' in fruits:
    print("APPLESSSSSS")
if 'strawberries' in fruits:
    print("Plenty of vitamin D in strawberries!")
if 'lemon' in fruits:
    print("Really, lemons are a favorite?")    
if 'blueberries' in fruits:
    print("I like blueberries too")


##################################
print('\n5-8. Hello Admin')
print('=========================')
usernames = ['admin', 'user1', 'user2','user3','user4']
##usernames = []
if len(usernames) <= 0:
    print('We have no users!')
for i in usernames:
    if i == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + i + ', nice to see you logged in today.')
        

print('\n5-10. Checking Usernames')
print('=========================')
current_users = ['user0', 'user1', 'user2','user3','user4']
new_users = ['NewUser0', 'NewUser1', 'NewUser2','user0','user1']

low_users = [x.lower() for x in current_users]
low_n_users = [y.lower() for y in new_users]

print(low_users)
print(low_n_users)

for j in low_n_users:
    if j in low_users:
        print('Sorry username ' + j + ' has been taken.\nPlease enter a new username.\n')
    else:
        print('That username is available\n')
        
    
print('\n5-11. Ordinal Numbers')
print('=========================')
numbs = [1,2,3,4,5,6,7,8,9]
##print(numbs)
for i in numbs:
    if i == 1:
        print(str(i) + 'st')
    elif i == 2:
        print(str(i) + 'nd')
    elif i == 3:
        print(str(i) + 'rd')
    elif i > 3:
        print(str(i) + 'th')
