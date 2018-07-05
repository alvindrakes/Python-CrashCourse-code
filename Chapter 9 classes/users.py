# 9.3 users

class User():
    """info about the User"""
    def __init__(self, first_name, last_name, age, gender):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.gender = gender

    def describe_user(self):
        print("My name is " + self.first_name.title() + " " + self.last_name.title())
        print("I am currently " + str(self.age) + " years old.")
        print("I am a " + self.gender)

    def greet(self):
        print("\nHello " + self.first_name.title() + " " + self.last_name.title())
        print("Welcome to No Man's Sky")

my_user = User("Alvin", "drakes", 20, "male")
my_user.describe_user()
my_user.greet()
