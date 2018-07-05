# using set in dictionary to reduce repetition

favourite_languages = {
        'sarah' : 'c',
        'john' : 'python',
        'kon' : 'ruby',
        'shawn' : 'go',
        'bob' : 'python'
        }

print("The following programming languages are mentioned:")
for language in set(favourite_languages.values()):
                # use set() function to reduce duplicates when printing  
                     
    print(language.title())