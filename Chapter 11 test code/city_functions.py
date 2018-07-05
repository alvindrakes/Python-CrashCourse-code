# 11.1 city country

def city_country(city_name, country_name, population = ''):
    """show in a city, country, population string form"""
    if population:
        full = city_name + ' ' + country_name + " population: " + str(population)
    else:
        full = city_name + ' ' + country_name

    return full.title()