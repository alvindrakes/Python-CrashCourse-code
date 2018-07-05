# 9.9 Battery upgrade

class Car():
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has" + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def inrement_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery from an electric car"""

    def __init__(self, battery_size = 70):
        """Initialize the battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """print statement describing the battery size"""
        print("This car has a " + str(self.battery_size) + "_kwh battery.")

    def get_range(self):
          """Print a statement about the range this battery provides"""
          if self.battery_size == 70:
              range = 240
          elif self.battery_size == 85:
              range = 270

          message = "This car can go approximately " + str(range)
          message += " miles on a full charge."
          print(message)

    def upgradeBattery(self):
        if self.battery_size != 85:
            self.battery_size = 85



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car 
        """

        super().__init__(make, model, year) #super function to make connections btw parent and child class
        self.battery = Battery()

  
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgradeBattery()
my_tesla.battery.get_range()