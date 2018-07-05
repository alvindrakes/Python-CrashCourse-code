Lincy = {
    'pet_name' : 'lincy',
    'animal_type' : 'lion',
    'owner_name' : 'john',
    }         

Kackit = {
    'pet_name' : 'kackit',
    'animal_type' : 'dog',
    'owner_name' : 'jaden',
    }         

boby = {
    'pet_name' : 'boby',
    'animal_type' : 'cat',
    'owner_name' : 'cindy',
    }        

pets = [Lincy, Kackit, boby]

for pet in pets:
    print("My name is " + pet['pet_name'].title() + ", my animal type is " + pet['animal_type'] +
        " and my owner is " + pet['owner_name'].title() + ".\n" )