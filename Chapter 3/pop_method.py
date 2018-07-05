# removing element using pop() method 

motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

popped_motorcycles = motorcycles.pop()       # pop the last element in the list and store it in a variable 
print (motorcycles)                          # to show that last element has been removed 
print (popped_motorcycles)                   # but we still have acces to the removed element using this variable 'popped_motorcycles'



# useful example of using pop() is to show the last item that you own in the list 

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()

print ("The last motorcycle that I owned was a " + last_owned + ".")


# pop item from any position on the list 

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print ("The first motorcycle that I owned was a " + first_owned + ".")

# use 'del' statement if not using the item in the future, while use 'pop()' method if wnat to access or use  the deleted item 