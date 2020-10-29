print('\nChapter 7: User Input and While Loops')
print('================================')

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name: "
# name = input(prompt)
# print(f"\nWhy hello there {name}!")

# age = input("How old are you? ")
# print(f"You are {age}!")


# # rollercoaster.py
# height = input("How tall are you, in inches? ") 
# height = int(height)
# if height >= 48: 
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older or taller.")


# Exercises
# print('\n 7-1. Rental Car')
# print('================================')
# car = input("Hello, what rental car would you like? ")
# print(f"Let me see if I can find you a {car}.")
<<<<<<< HEAD
# 
# print('\n 7-2. Restaurant Seating')
# print('================================')
# party = input("Hello, how many people are in your group? ")
# if int(party) > 8:
    # print("You will have to wait a few minutes for a table.")
# else:
    # print("Lucky for you, we have a table ready.")
# 
# 
# print('\n 7-3. Multiples of Ten')
# print('================================')
# tens = input("Enter a number to determine if its a multiple of ten: ")
# if int(tens) % 10 == 0:
    # print(f"Your number {tens} is indeed a multiple of ten.")
# else:
    # print(f"{tens} is not a multiple of ten")
# 
# Using continua in a loop
# counting.py
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)

print('\n 7-4. Pizza Toppings')
print('================================')
prompt = "\nWhat kind of topping would you like? "
prompt += "\n(Enter 'quit' when done.) "

while True:
    top = input(prompt)
    if top == 'quit':
        break
    else:
        print(f"{top.title()} will be added to the pizza order.")



print('\n 7-5. Movie Tickets')
print('================================')
age = input("Welcome to the Movie Theater! \nHow old are you?: ")

if age < 3:
    print("Your ticket is free!")
    elif age >= 3 and age < 12:
        print("That will be $10.")
        elif age >= 12:
            print("That will be $15 oldie.")
            
=======

# print('\n 7-2. Restaurant Seating')
# print('================================')
# party = input("Hello, how many people are in your group? ")
# if int(party) > 8:
#     print("You will have to wait a few minutes for a table.")
# else:
#     print("Lucky for you, we have a table ready.")


# print('\n 7-3. Multiples of Ten')
# print('================================')
# tens = input("Enter a number to determine if its a multiple of ten: ")
# if int(tens) % 10 == 0:
#     print(f"Your number {tens} is indeed a multiple of ten.")
# else:
#     print(f"{tens} is not a multiple of ten")

# parrot.py
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. \n"
# message = " "
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# cities.py good break demonstration
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)


    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
>>>>>>> fd5a5e20af2de12328f10ce55f537f52bb3b3b38
