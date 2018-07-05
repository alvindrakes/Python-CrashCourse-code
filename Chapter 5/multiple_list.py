# using multiple list 

available_toppings = ['mushroom', 'peperroni', 'chicken', 'beef', 'pepper']

requested_toppings = ['mushroom', 'ice cream', 'nigga', 'beef']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + ' to the pizza.')
    else:
        print('Sorry sir, we don''t have ' + requested_topping + ' at the moment')


print('\nFinished making your pizza!')