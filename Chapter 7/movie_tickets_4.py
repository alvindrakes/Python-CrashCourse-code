# use 'quit' to end programme

while True:

    age = ("\nWhat is your age?\n")
    age += ("Enter 'quit' to end the programme\n")

    try:

        real = int(input(age))

        if real > 12:
            print("The ticket price is 15$.")



        if real >= 3 and real <= 12:
            print("The ticket price is 10$")


        if real < 3:
             print("The ticket is free!")

    except ValueError:     #if the input entered is a string not integer, just stop the programme
        break



