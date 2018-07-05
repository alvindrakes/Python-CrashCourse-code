# 10.7 addition calculator

print("Please enter 2 numbers to be added.")
print("Enter 'q' to quit the program.")

while True:

    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break

    second_num = input("Second number: ")
    if second_num == 'q':
        break

    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print("Sorry the input you have given is not a number.")
    else:
        print(str(answer))