# 5.1 conditional test 

requested_toppings = ['mushrooms', 'chicken', 'beef', 'peperroni', 'fish'
						, 'steak', 'pork']


print('Me: I would like to order a pizza ')
print('Waiter: Of course sir, what toppings would you like?')
print('Me: I want all these toppings:')
for topping in requested_toppings:
	print(topping)

print('Waiter: Would you like to add anchovies,sir ?')

if requested_toppings != 'anchovies':
	print('Me: NO! I hate anchovies')
else:
	print('Me: yes sure thing')

print('Waiter: is a hot day, would you like a cup of lemonade?')

hot_day_drink = ['lemonade', '100 plus', 'coca-cola']

print('Me: could you show me more drinks ?')
print('Waiter: of course sir ... here is the menu\n')

print('*************************')
print('\t\tMENU\n')
for drink in hot_day_drink:
	print(drink)
print('*************************\n')

print('Me: ok, I think I''ll still have the ' + hot_day_drink[0] + '.')
print('Waiter: Thank you for your orders, sir.')
print('Me: Thank you for being patient.')
