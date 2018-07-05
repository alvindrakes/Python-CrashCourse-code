# 7.10 dream vacation

dream_vacation = {}

active = True

while active:

    name = input("\nWhat is your name? ")
    answer = input("If your could travel the world, which place would you like to travel first? ")

    dream_vacation[name] = answer

    check = input("Any poll left? (yes/no) ")
    if check == 'no':
        active = False

print("\n--------Dream Vacation----------")
for name, answer in dream_vacation.items():
    print(name + " would like to travel to " + answer)