# 9-1. Restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Restaurant cuisine description"""
        print(f"{self.name} is a {self.cuisine} restaurant.")

    def open_restaurant(self):
        """Print method for the restaurant."""
        print(f"{self.name} is currently opened for business.")

    def read_number_served(self):
        """Simply reads the number of customers served."""
        print(f"{self.name} has served {self.number_served} customers.")

    def set_number_served(self, customers_served):
        """Set the number of people served."""
        self.number_served = customers_served
        print(f"This restaurant has served {self.number_served} customers.")

    def increment_number_served(self, increment):
        if increment > 0:
            self.number_served += increment
            print(f"{self.name} has served {self.number_served} customers today.")
        else:
            print(f"{self.name} had no customers today.")

r1 = Restaurant("Panda Express", "Asian")
r1.describe_restaurant()
r1.open_restaurant()

print("\n9-3. Users\n==========================")

class User:
    def __init__(self, first_name, last_name, username, gender):
        self.first = first_name
        self.last = last_name
        self.username = username
        self.gender = gender
        self.country = "USA"
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first} {self.last} is {self.gender} and lives in {self.country}.")

    def greet_user(self):
        print(f"Welcome {self.first}. Hope today goes well.")

    def get_login_attempts(self):
        print(f"'{self.username}' has logged in {self.login_attempts} times.")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Login attempts = {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"The number of logins for '{self.username}' has been reset.")

u1 = User("Tahoma", "Ringo", "tringo123", "male")
u1.describe_user()
u1.greet_user()


print("\n9-4. Number Served\n==========================")

restaurant2 = Restaurant("Guilbertos", "Mexican")
restaurant2.read_number_served()
restaurant2.set_number_served(50)
restaurant2.increment_number_served(10)
restaurant2.increment_number_served(-5)

print("\n9-5. Login Attempts\n==========================")
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.get_login_attempts()
u1.reset_login_attempts()
u1.get_login_attempts()


print("\n9-6. Ice Cream Stand\n==========================")

class IceCreamStand(Restaurant):
    """Represents an ice cream stand version of a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class."""
        # Note there is no self in the super
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "strawberry", "vanilla"]

    def get_flavors(self):
        print(f"\nOur ice cream flavors include:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Name of restaurant
ice_stand = IceCreamStand("ColdStone", "Dessert")
# Using methods from parent class (Restaurant)
ice_stand.describe_restaurant()
ice_stand.read_number_served()
ice_stand.set_number_served(90)
ice_stand.increment_number_served(20)
# Using methods from child class (IceCreamStand)
ice_stand.get_flavors()

# class Privileges():
#     def __init__(self):
#         self.privs = ["can add post", "can delete post",
#         "can add user", "can ban user"]

#     def show_privileges(self):
#         print(f"Admin privileges include:")
#         for privilege in self.privs:
#             print(f"- {privilege}")

# class Privileges():
#     def __init__(self, first_name, last_name, username, gender):
#         super().__init__(first_name, last_name, username, gender)        
#         self.privs = ["can add post", "can delete post",
#         "can add user", "can ban user"]

#     def show_privileges(self):
#         print(f"Admin privileges include:")
#         for privilege in self.privs:
#             print(f"- {privilege}")


print("\n9-7. Admin\n==========================")
class Admin(User):
    """Represents a different user known as Administrator"""
    def __init__(self, first_name, last_name, username, gender):
        self.privileges = Privileges
        # self.privileges = ["can add post", "can delete post",
        # "can add user", "can ban user"]

    # def show_privileges(self):
    #     print(f"Admin privileges include:")
    #     for privilege in self.privileges:
    #         print(f"- {privilege}")

# lex97 = Admin("Lex", "Luthor", "LLKing_su", "male")

# # Calling methods from parent class (User)
# lex97.greet_user()
# lex97.describe_user()
# Calling methods from child class (Admin)
# lex97.show_privileges()


print("\n9-8. Privileges\n==========================")
# Write a separate Privileges class. The class should have one
# attribute, privileges , that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges instance
# as an attribute in the Admin class. Create a new instance of Admin and use your
# method to show its privileges.
class Privileges():
    def __init__(self, privileges)
    # def __init__(self, first_name, last_name, username, gender):
        self.privileges = ["can add post", "can delete post",
        "can add user", "can ban user"]

    def show_privileges(self):
        print(f"Admin privileges include:")
        for privilege in self.privileges:
            print(f"- {privilege}")

rosa98 = Admin("Rosa", "Line", "rosal_su", "female")
rosa98.show_privileges()
# rosa98.greet_user()
# rosa98.describe_user()