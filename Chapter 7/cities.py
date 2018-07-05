prompt = "\nPlease enter the cities you have visited"
prompt += "\nEnter 'quit' when you're finished\n"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I would love yo go to " + city + "!")

