# 9.5 Login attempts

class User():
    """info about the User"""
    def __init__(self, first_name, last_name, age, gender):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
       self.gender = gender
       self.login_attempts = 0

    def describe_user(self):
        print("My name is " + self.first_name.title() + " " + self.last_name.title())
        print("I am currently " + str(self.age) + " years old.")
        print("I am a " + self.gender)

    def greet(self):
        print("\nHello " + self.first_name.title() + " " + self.last_name.title())
        print("Welcome to No Man's Sky")

    def increment_login_attempts(self):
        """increment login attempts by 1"""
        self.login_attempts += 1
        print("Login attempts: " + str(self.login_attempts))

    def reset_login_attempts(self):
        """reset the login attempts to 0"""
        self.login_attempts = 0
        print("Login attempts: " + str(self.login_attempts))


my_user = User("Alvin", "drakes", 20, "male")
my_user.describe_user()
my_user.greet()

another_user = User("jaden", "bro", 20, "male")
another_user.increment_login_attempts()
another_user.increment_login_attempts()
another_user.increment_login_attempts()
another_user.reset_login_attempts()


