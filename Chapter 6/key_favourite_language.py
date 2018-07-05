favourite_languages = {
        'sarah' : 'c',
        'john' : 'python',
        'kon' : 'ruby',
        'shawn' : 'go',
        }


friends = ['kon', 'shawn']


for name in favourite_languages.keys():   # keys() function just to print key
    print(name.title())

    if name in friends:
        print('     Hi ' + name.title() + '! I see your favourite language is' +
            favourite_languages[name].title() + '.')

if 'erin' not in favourite_languages.keys():
    print('Erin, come and take our poll!')

