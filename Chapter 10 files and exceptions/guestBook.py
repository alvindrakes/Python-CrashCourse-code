# 10.4 guest book

while True:
    names = "\nPlease enter your name: "
    names += "\nEnter 'quit' to quit this program\n"

    filename = "guest_book.txt"

    name = input(names)

    with open(filename, 'a') as file_object:
        file_object.write("\n")
        file_object.write(name)
        file_object.write("\nWelcome aboard, " + name + "!\n")

    if name == 'quit':
        break