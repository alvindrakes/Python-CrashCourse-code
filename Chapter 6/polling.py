#6.6 polling 

favourite_languages = {
        'sarah' : 'c',
        'john' : 'python',
        'kon' : 'ruby',
        'shawn' : 'go',
        }

name_list = ['katie', 'bob', 'carie', 'weilu', 'kon', 'sarah']

for name in name_list:
    if name in favourite_languages.keys():
        print("Thank you for taking the poll " + name + '!')
    else:
        print("Please remember to take the toll " + name + '.')



