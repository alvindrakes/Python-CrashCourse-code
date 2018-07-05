# 9.1 restaurant

class Restaurant():
    """Model restaurant menu"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant is filled with muscular guys and steaks!")
        
    def open_restaurant(self):
        print("The restaurant is now officially open!")

my_restaurant = Restaurant("SaltBae", "Steak and Grilled")

print(my_restaurant.name.title())
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
       