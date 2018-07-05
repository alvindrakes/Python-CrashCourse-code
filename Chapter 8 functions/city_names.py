# 8.6 city names

def city_names(city, country):
    formatted = "\"" + city + ", " + country + "\""
    return formatted.title()

city1 = city_names('kajang', 'malaysia')
city2 = city_names('new york', 'usa')
city3 = city_names('delhi', 'india')

print(city1)
print(city2)
print(city3)