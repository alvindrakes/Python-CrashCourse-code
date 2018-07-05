#three restaurants

class Restaurant():
    """Model restaurant menu"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant is filled with muscular guys and steaks!")
        
    def open_restaurant(self):
        print("The restaurant is now officially open!")

