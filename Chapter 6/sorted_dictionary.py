# sorted dictionary 

favourite_languages = {
        'sarah' : 'c',
        'john' : 'python',
        'kon' : 'ruby',
        'shawn' : 'go',
        }

for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking our poll!")