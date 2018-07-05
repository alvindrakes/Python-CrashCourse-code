# defining a function

def greet_user(username):    # use keyword "def" to tell python that you're defining a function
    """Display a simple greeting"""   #this is a docstring, important for python documentation!
    print("Hello " + username.title() + "!" )

greet_user('Alvin')