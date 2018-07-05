#if a function need to accept different arguments, abitrary argument will be placed at the back


def make_pizza(size, *toppings):  #this is called abitrary arguments
    """Summarize the toppings added onto the pizza"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print(" -" + topping)

make_pizza(6, "Mushroom")
make_pizza(8, "peperoni", "Chilli", "pepper")