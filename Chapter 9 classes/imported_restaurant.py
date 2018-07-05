# 9.10 imported restaurants

from restaurants_2 import Restaurant


my_restaurant = Restaurant("SaltBae", "Steak and Grilled")
second_restaurant = Restaurant("KFC", "fried chickens")
third_restaurant = Restaurant("VeganCorner", "vegetarion foods")

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