# greeter 

# the symbol += add the new line to the end of variable prompt woth space
prompt = "If you tell us your name, we can peronalize this message for you.\n"
prompt += "So what is your name: "

name = input(prompt)

print("Hello " + name.title() + "!")