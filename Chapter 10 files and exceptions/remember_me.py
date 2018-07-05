import json

filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
      

except FileNotFoundError:
    username = input("What is your name? ")


    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("we will remember you when you are back, " + username)


else:
    entered_user = input("Please enter your name to verify: ")
    if entered_user == username:
        print("\nWelcome back, " + username + "!")
    else:
        print("\nI am sorry you are not allowed to access this system.")