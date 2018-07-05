# 8.12 sandwiches

def thingsOnSandwich(*stuffs):
    """print out the toppings on the sandwich"""
    print("\nToppings on sandwich: ")
    for stuff in stuffs:
        print(stuff)


thingsOnSandwich("Pepper")
thingsOnSandwich("Chili", "apple", "orange")
thingsOnSandwich("mushroom", "carrot")