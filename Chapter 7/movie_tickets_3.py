active = 0   #use count to stop loop

while active < 3:

    age = input("\nWhat is your age?\n")

    age = int(age)

    if age > 12:
        print("The ticket price is 15$.")
        active +=1


    if age >= 3 and age <= 12:
        print("The ticket price is 10$")
        active += 1

    if age < 3:
        print("The ticke is free!")
        active += 1