from user_module import User
from privilege_module import Privilege

class Admin(User):
    """list of admin attributes"""
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privilege = Privilege()
