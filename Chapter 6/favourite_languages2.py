# favourite languages

# with list inside dictionary, user can have multiple favourite languages
favourite_languages = {
    'jen' : ['ruby', 'pascal'],
    'john' : ['python'],
    'jack' : ['c'],
    'jacob' : ['c++', 'swift']
    }

for name, languages in favourite_languages.items():
    print("\n" + name.title() + " love the language: ")
    for language in languages:
        print("\t" + language.title())
        