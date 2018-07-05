prompt = "\nTell me something and I'll repeat them back to you: "

prompt += "\nEnter 'quit' to end the program \n"

# The active variable act as a flag to indicate when to start and stop the while loop
active = True

message = ""


while active:
    message = input(prompt)

    if message == 'quit':
        active = False

    else:
        print(message)