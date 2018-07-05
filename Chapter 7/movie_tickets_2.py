active = True    #use variable to stop loop

while active:

    age = input("\nWhat is your age?\n")

    age = int(age)

    if age > 12:
        print("The ticket price is 15$.")
        active = False

    if age >= 3 and age <= 12:
        print("The ticket price is 10$")
        active = False

    if age < 3:
        print("The ticke is free!")
        active = False