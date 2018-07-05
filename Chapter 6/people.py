# 6.7 people

person_info1 = {
    'place' : 'sungai long',
    'age' : '20',
    'hobby' : 'learning new stuff',
    'first_name' : 'loh', 
    'last_name' : ' jin xian',
    }

person_info2 = {
    'place' : 'New york',
    'age' : '22',
    'hobby' : 'coding',
    'first_name' : 'jaden', 
    'last_name' : ' drakes',
    }

person_info3 = {
    'place' : 'miami',
    'age' : '25',
    'hobby' : 'observe plants',
    'first_name' : 'kon', 
    'last_name' : ' jian yang',
    }

people = [person_info1, person_info2, person_info3]

for person in people:
    print('\nHi! My name is ' + person['first_name'] + person['last_name']
    + ', I am ' + person['age'] + ' years old.')
    print('My hobby is ' + person['hobby'] + ' and I live in '
    + person['place'] + '.')    
    