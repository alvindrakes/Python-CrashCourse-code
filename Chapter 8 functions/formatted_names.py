def get_formatted_name(first_name, last_name, middle_name=''):  #put an empty string to make a parameter optional
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
        return full_name.title()
    else:
        full_name = first_name + " " + last_name
        return full_name.title()

musician = get_formatted_name('alvin', 'drakes')
print(musician)

popcorn = get_formatted_name('alvin', 'drakes', 'steve')
print(popcorn)