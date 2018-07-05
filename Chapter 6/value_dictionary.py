# acceess only the values in dictionaries

favourite_languages = {
        'sarah' : 'c',
        'john' : 'python',
        'kon' : 'ruby',
        'shawn' : 'go',
        }

print("The following programming languages are mentioned:")
for language in favourite_languages.values():
                                   # use values() for accessing value only
    print(language.title())

for language in favourite_languages.keys():
    
