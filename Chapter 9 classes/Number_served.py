# 9.4 Number served

class Restaurant():
    """Model restaurant menu"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant is filled with muscular guys and steaks!")
        
    def open_restaurant(self):
        print("The restaurant is now officially open!")

    def set_number_served(self, number):
        """set the number of customers served"""
        self.number_served = number

    def increment_number_served(self, increment):
        """increment the number of customers served"""
        self.number_served += increment

    def customers_served(self):
        print("My restaurant has served " + str(self.number_served) + " customers.")


my_restaurant = Restaurant("SaltBae", "Steak and Grilled")

print(my_restaurant.name.title())
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(100)
my_restaurant.customers_served()

my_restaurant.increment_number_served(10)
my_restaurant.customers_served()

