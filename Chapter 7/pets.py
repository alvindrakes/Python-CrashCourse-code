# remove all instances of specific value at once

animals = ['dog', 'cat', 'elephant', 'cat', 'monkey', 'lion']
print(animals)

while 'cat' in animals:

    animals.remove('cat')

print(animals)