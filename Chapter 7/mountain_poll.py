responses = {}

# create a flag to indicate the poll is active
poll_active = True

while poll_active:
    # prompt for person's name and responses
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # store the response in the doctionary
    responses[name] = response

    # check if nayone still want to take the poll
    repeat = input("Anyone would like take the poll? (yes/no) ")
    if repeat == 'no':
        poll_active = False

    # polling complete, show results

print("\n-------Poll result--------")
for name, response in responses.items():
    print(name + " would like to climb " + response)