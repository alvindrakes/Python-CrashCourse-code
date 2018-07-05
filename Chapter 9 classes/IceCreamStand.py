# 9.6 ice cream stand

#three restaurants

class Restaurant():
    """Model restaurant menu"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant is filled with muscular guys and steaks!")
        
    def open_restaurant(self):
        print("The restaurant is now officially open!")

class IceCreamStand(Restaurant):
    """model a ice cream stand in the restaurant"""

    def __init__(self, name, cuisine_type):
        """initialize attributes of iceCreamStand"""
        super().__init__(name, cuisine_type)

    def decribe_flavor(self):

        flavor = ["strawberry", "chocolate", "vanilla", "oreo"]
        for flavors in flavor:
            print("The available ice cream flavors are " + flavors)


my_restaurant = Restaurant("SaltBae", "Steak and Grilled")
second_restaurant = Restaurant("KFC", "fried chickens")
third_restaurant = Restaurant("VeganCorner", "vegetarion foods")
stand1 = IceCreamStand("Kita", "ice cream")

print(my_restaurant.name.title())
print(my_restaurant.cuisine_type)
print("\n" + second_restaurant.name.title())
print(second_restaurant.cuisine_type)
print("\n" + third_restaurant.name.title())
print(third_restaurant.cuisine_type + "\n")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
second_restaurant.describe_restaurant()
second_restaurant.open_restaurant()
third_restaurant.describe_restaurant()
third_restaurant.open_restaurant()
stand1.decribe_flavor()

