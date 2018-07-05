# 9.12 multiple modules

from privilege_module import Privilege
from user_module import User
from admin_module import Admin



my_user = User("Alvin", "drakes", 20, "male")
Admin_1 = Admin("Boss", "Baby", 22, "male")
Admin_2 = Admin("Nigga", "bro", 30, "male")
my_user.describe_user()
my_user.greet()
#Admin_1.get_privileges()
Admin_2.privilege.get_privileges()