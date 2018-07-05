# 6.11 cities 

cities = {
    'shanghai' : {
        'country' : 'china',
        'population' : '14.35 million',
        'fact' : 'a modern city',
        },

    'abu dhabi' : {
        'country' : 'dubai',
        'population' : '613,368',
        'fact' : 'one of the richest city in the world',
        },

    'kuala lumpur' : {
        'country' : 'malaysia',
        'population' : '1.589 million',
        'fact' : 'a city with multiple races',
        },
    }

# just use the value and enter the key in the value, facts['country'] etc
for name, facts in cities.items():
    print("City name: " + name.title())
    print( "This city is located in " + facts['country'].title() + 
        ". It's population size is " + str(facts['population']) +
        ". One fun fact about this city is " + facts['fact'] + ".\n" )
    


