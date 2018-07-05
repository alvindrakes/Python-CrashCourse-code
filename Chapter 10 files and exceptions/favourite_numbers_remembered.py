# 10.12 favourite numbers remmebered


import json

filename = 'favourite.json'

try:
    with open(filename) as f_obj:
        number = json.load(f_obj)

except FileNotFoundError:

    print("Tell me what is your favourite number.")

    favourite_num = input("Favourite number: ")

    filename = 'favourite.json'
    with open(filename, 'w') as f_obj:
        json.dump(favourite_num, f_obj)

else: 

    print("Haha I know your favourite number is " + number)




