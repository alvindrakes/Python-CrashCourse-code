ask = "\nWhat pizza toppings would you like to be added?"
ask += "\nEnter 'quit' to end the program\n"


pizza_topping = ""

while True:

    pizza_topping = input(ask)

    if ask == 'quit':
        break
    else:
        print("I have added " + pizza_topping + " on you pizza")