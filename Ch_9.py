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


class User:
    def __init__(self, first_name, last_name, username):
        self.first = first_name
        self.last = last_name
        self.username = username
        
        

print("\n9-4. Number Served\n==========================")

restaurant2 = Restaurant("Guilbertos", "Mexican")
restaurant2.read_number_served()
restaurant2.set_number_served(50)
restaurant2.increment_number_served(10)
restaurant2.increment_number_served(-5)

print("\n9-5. Login Attempts\n==========================")