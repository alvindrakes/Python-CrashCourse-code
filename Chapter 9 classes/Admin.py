# 9.7 Admin

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

class Admin(User):
    """list of admin privileges and attributes"""
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)

    def get_privileges(self):
        privileges = ["can add post", "can edit content", "can ban user"]

        for privilege in privileges:
            print("Admin " + privilege)



my_user = User("Alvin", "drakes", 20, "male")
Admin_1 = Admin("Boss", "Baby", 22, "male")
my_user.describe_user()
my_user.greet()
Admin_1.get_privileges()