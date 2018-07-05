import json

filename = 'favourite.json'
with open(filename) as f_obj:
    number = json.load(f_obj)

print("Haha I know your favourite number is " + number)