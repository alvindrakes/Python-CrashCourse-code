class Dog():
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")


#create an instance of the class
my_dog = Dog("Jacob", 8)
your_dog = Dog("Kata", 7)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over() #after creating an instance, we can call any method defined in Dog class

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog's age is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
        