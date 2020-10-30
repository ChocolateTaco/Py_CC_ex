# # Ch 8
# print("8-7. Album\n==================================")
# def make_album(artist, title, num_songs = None):
#     """Return a dictionary of an artist's music album."""
#     alb = {'Artist': artist, 'Album Name': title}
#     if num_songs:
#         alb['Number of songs'] = num_songs
#     return alb

# cold = make_album('Boy in Space', 'Live EP', 7)
# print(cold)
# dovecam = make_album('Dove Cameron', 'Bloodshot/Waste')
# print(dovecam)


# print("8-8. User Albums\n==================================")
# while True:
#     a = input('\nEnter a name of a musical artist: ')
#     print("  (enter 'q' at any time to quit)")

#     if a == 'q':
#         break

#     b = input('Enter a name of one of their albums: ')
#     print("  (enter 'q' at any time to quit)")
#     if b == 'q':
#         break

#     response = make_album(a,b)
#     print(response)

# print("8-9. Messages \n==================================")
# msgs = ["Hey", "What's up?", "Where are we going?", "When are we going?"]
# def show_messages(message):
#     for message in message:
#         print(message)

# show_messages(msgs)


# print("8-10. Sending Messages \n==================================")
# msgs = ["Hey", "What's up?", "Where are we going?", "When are we going?"]
# sent = []
# def send_messages(x):
#     while x:
#         sending = x.pop()
#         print(sending)
#         sent.append(sending)

# send_messages(msgs)
# print("\n\n")
# print(f"Original message list: {msgs}")
# print(f"Sent text messages: {sent}")


# print("8-11. Archived Messages \n==================================")
# msgs = ["Hey", "What's up?", "Where are we going?", "When are we going?"]
# sent = []
# def send_messages(x):
#     while x:
#         sending = x.pop()
#         print(sending)
#         sent.append(sending)

# send_messages(msgs[:])          # [:] allows the function to use a copy of the input value(s)
# print("\n\n")
# print(f"Original message list: {msgs}")
# print(f"Sent text messages: {sent}")


# print("8-12. Sandwiches \n==================================")

# def sammich_order(*ingredients):
#     print("\nYour sandwich order includes: ")
#     for ingredient in ingredients:
#         print(f"* {ingredient}")

# sammich_order('tomatoes', 'mayo', 'pickles')
# sammich_order('tomatoes', 'mayo', 'pickles', 'ham', 'lettuce', 'eggs')
# sammich_order('tomatoes', 'bacon', 'lettuce')


print("8-13. User Profile \n==================================")
def build_profile(first, last, **user_info): 
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Chocolate', 'Tacos', location='Freezer', 
    field='Dessert', flavor='Neopolitan')
print(user_profile)


print("8-14. Cars \n==================================")

def make_car(make, model, **other):
    other['make'] = make
    other['model'] = model
    return other

car = make_car('subaru', 'outback', color='blue', towpackage=True)
print(car)

print("8-15. Cars \n==================================")





