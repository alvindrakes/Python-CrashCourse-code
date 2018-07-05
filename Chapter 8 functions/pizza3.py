# using import in python

def make_pizza(size, *toppings):  #this is called abitrary arguments
    """Summarize the toppings added onto the pizza"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print(" -" + topping)
