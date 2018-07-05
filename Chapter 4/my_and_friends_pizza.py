# 4.11 my pizza, your pizza 


pizza_names = ['chicken cheese', 'peperroni', 'hawaii chicken']
friends_pizzas = pizza_names[:]

pizza_names.append('seafood delight')
friends_pizzas.append('barbeque beef')


print ("My favourite pizzas are:")
for pizza in pizza_names:
	print(pizza)


print ("\nMy friends' favourite pizzas are:")
for friend_pizza in friends_pizzas:
	print(friend_pizza)