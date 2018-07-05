# 6.10 favourite numbers


favourite_numbers = {
    'shawn' : [6,7,5,9,10],
    'jaden' : [8,23,3456,6587],
    'kon' : [9,23,54,21],
    'alvin' : [7,123,123],
    'jack' : [5,123,432],
    }

# loop the dictionary and print statement
for name, numbers in favourite_numbers.items():
    print(name.title() + ' loves the number: ')
    for number in numbers:
        print("\t" + str(number))
    