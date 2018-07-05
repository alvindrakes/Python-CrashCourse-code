# tuples 

# tuples is an immutable list, which means the list cannot be changed 

dimensions = (200, 50)  # we define a tuple by using parentheses

print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250  # error if we try to change 1 of the items in tuple dimensions

print('\nOriginal dimensions:')
for dimension in dimensions:
	print(dimension)

dimensions = (400, 40)         # just redefine the tuples if you want to change the value 

print('Modified dimensions:')
for dimension in dimensions:
	print(dimension)