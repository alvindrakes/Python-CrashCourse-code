squares = []

for value in range(1,11):
	# square = value ** 2
	# squares.append(square)

	# or we can do it this way 
	squares.append(value ** 2)   # directly do the calculation inside the list 

print(squares)

# list comprehension 

squares_2 = [value ** 2 for value in range(1,11)]
print(squares_2)