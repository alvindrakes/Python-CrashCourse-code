# 6.5 rivers

rivers = {
    'nile' : 'egypt',
    'sungai long' : 'kajang',
    'jungle river' : 'amazon',
    }

for river, country in rivers.items():
    print('The ' + river + ' runs through ' + country + '.')

for river in rivers.keys():
    print("Name of river: " + river)

for country in rivers.values():
    print("Country name: " + country)