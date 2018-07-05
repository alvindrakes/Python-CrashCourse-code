class Privilege():
    """list of Admin's prvileges"""
    def __init__(self,  privileges = ["can add post", "can edit content", "can ban user"] ):
        self.privileges = privileges

    def get_privileges(self):
       
        for privilege in self.privileges:
            print("Admin " + privilege)