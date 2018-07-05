# 5.2 more conditional test

# 1
car = 'bmw'
if car == 'bmw':
	print('True')

car = 'ferrari'
if car == 'bmw':
	print('True')
else: 
	print('False')

# 2
bro = 'CHAN'
if bro.lower() == 'chan':
	print('That''s my bro')


#3
number1 = 5
number2 = 10
if number2 >= number1:
	print("you are right")
else:
	print('You are wrong')

#4
if number1 and number2 >1:
	print('That is a big number')

if number2 or number1 >= 10:
	print('haha')

#5
cars = ['bmw', 'ferrari', 'mercedez', 'vw']
if 'bmw' in cars:
	print(cars[0].upper() + ' is in the Hood!')

#6
cars = ['ferrari', 'mercedez', 'vw']
if 'bmw' not in cars:
	for car in cars:
		if car == 'vw':
			print('VW is destroying BMW')
		else:
			print(car.title() + ' is destroying BMW')

	