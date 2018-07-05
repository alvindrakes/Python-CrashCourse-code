# cars

def make_car(manufacturer, car_model, **additional_info):
    """Print all the information about the car"""
    car_info = {}
    car_info['Manufacturer'] = manufacturer
    car_info["Car Model"] = car_model
    for key, value in additional_info.items():
        car_info[key] = value
    return car_info

car = make_car('Subaru', 'Outback', colour = 'blue', tow_package = 'True')
print(car)
