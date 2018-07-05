with open('pi_digits.txt') as file_object:
  #  for line in file_object:
  #       print(line.rstrip())

  lines = file_object.readlines()

for line in lines:
    print(line)
