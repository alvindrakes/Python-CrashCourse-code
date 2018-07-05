# imported Admins

from Privileges import User, Privilege, Admin


my_user = User("Alvin", "drakes", 20, "male")
Admin_1 = Admin("Boss", "Baby", 22, "male")
Admin_2 = Admin("Nigga", "bro", 30, "male")
my_user.describe_user()
my_user.greet()
#Admin_1.get_privileges()
Admin_2.privilege.get_privileges()