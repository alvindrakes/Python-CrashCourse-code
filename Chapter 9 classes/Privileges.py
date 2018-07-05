# 9.8 privileges

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


class Privilege():
    """list of Admin's prvileges"""
    def __init__(self,  privileges = ["can add post", "can edit content", "can ban user"] ):
        self.privileges = privileges

    def get_privileges(self):
       
        for privilege in self.privileges:
            print("Admin " + privilege)



class Admin(User):
    """list of admin attributes"""
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privilege = Privilege()

    
