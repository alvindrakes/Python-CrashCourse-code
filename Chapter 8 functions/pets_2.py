# keyword arguments
# name-value pair argument, will not have confusing result

def describe_pet (pet_name, animal_type='dog'): # specify a default value for the parameter, if no value provided, python will use default value
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())

describe_pet('harry')