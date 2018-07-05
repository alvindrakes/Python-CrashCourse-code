# 4.12 more loops 


my_food = ['veggies', 'tomatoes', 'apple']
friend_food = my_food[:]     


my_food.append('cheese')
friend_food.append('nugget')      

for food in my_food:
	print(food)

print('\n')
for friends in friend_food:
	print(friends)
