# checking for empty list

requested_toppings = []

if requested_toppings:

    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + '.')
    print('Your pizza is ready!')

else:
    print('Sir, do you want a plain pizza ?')
