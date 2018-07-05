# 10.6 addition 

print("Please enter 2 numbers to be added.")

first_num = input("First number: ")
second_num = input("Second number: ")

try:
    answer = int(first_num) + int(second_num)
except ValueError:
    print("Sorry the input you have given is not a number.")
else:
    print(str(answer))