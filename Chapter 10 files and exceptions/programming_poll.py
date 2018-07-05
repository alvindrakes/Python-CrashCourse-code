# 10.5 programming poll

message = "\nWhy do you like or love programming? "
message += "\nPlease list down the reasons.\n"
message += "Enter 'quit' when you are finished listing.\n"

while True:

    reasons = input(message)

    filename = "reactions.txt"

    with open(filename, "a") as file_object:
        file_object.write(reasons)
        file_object.write("\n")

    if reasons == 'quit':
        break