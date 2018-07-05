# sometimes uou don't know how many value does the function need to accept

def make_pizza(*toppings):  #this is called abitrary arguments
    """Summarize the toppings added onto the pizza"""
    print("\nTopings added:")
    for topping in toppings:
        print(" -" + topping)

make_pizza("Mushroom")
make_pizza("peperoni", "Chilli", "pepper")