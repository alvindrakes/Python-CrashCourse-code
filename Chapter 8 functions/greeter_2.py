# use a function in a while loop

def get_formatted_name(first_name, last_name):
    """Return formatted full name"""
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name; ")
    print("Press 'q' to quit the program")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello and welcome to gamer 2017, " + formatted_name + "!")