# returning a dictionary

def build_person(first_name, last_name, age=''):
    """Return a dictionary of info about a person"""
    person = {'first':first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

gamer = build_person('alvin', 'drakes', 20)
print(gamer)