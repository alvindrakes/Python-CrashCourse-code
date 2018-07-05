# checking for special item 

requested_toppings = ['mushroom', 'peperroni', 'chicken', 'beef']

for requested_topping in requested_toppings:
    if requested_topping == 'peperroni':
        print('Sorry sir, we are out of pepperoni.')
    else:
        print('Adding ' + requested_topping + '.')

print('\nYour delicious pizza is ready')