# copying list in python

my_food = ['veggies', 'tomatoes', 'apple']
friend_food = my_food[:]      # just omit the indexes to copy the entire list 

print('This is my food')
print(my_food)
print('\n')

print('This is my friend''s food')
print(friend_food)

my_food.append('cheese')
friend_food.append('nugget')          # as you can see, the 2 lists are seperated

print('\nThis is my food')
print(my_food)

print('\nThis is my friend''s food')
print(friend_food)


# THIS DOESN'T WORK (if we want seperate copy of lists, we need to use slices)
my_food = friend_food

my_food.append('cheese')
friend_food.append('nugget')         

print('\nThis is my food')
print(my_food)                    # as both my_food and friends_food print the same things 

print('\nThis is my friend''s food')
print(friend_food)

