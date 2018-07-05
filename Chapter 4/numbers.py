# range ()

for numbers in range(1,5):
	print (numbers)           # need to be careful with off-by-one error, range() start counting from the 1st value you give
	                          # and stop at the last 2nd value.
#--------------------------------------------------------------------------------------
	                          # so if want to print from 1 to 5, then do this:


for numbers in range(1,6):
	print (numbers)


numbers = list(range(1,6))    #by using the list function, we convert the range into a list 
print (numbers)