def greet_users2 (names):
    """Print a simple message to all users"""
    for name in names:
        print("Hello! Nice to meet you, " + name.title() + "!")

usernames = ["Alvin", "jaden", "Kon"]
greet_users2(usernames)