# 10.11 favourite numbers
import json

print("Tell me what is your favourite number.")

favourite_num = input("Favourite number: ")

filename = 'favourite.json'
with open(filename, 'w') as f_obj:
    json.dump(favourite_num, f_obj)