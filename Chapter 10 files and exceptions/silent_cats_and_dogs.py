# 10 .9 silent cats and dogs 

filenames = ['cats.txt', 'dogs.txt']

try:
    for filename in filenames:
        with open(filename) as file_object:
            contents = file_object.read()

        print(contents)

except FileNotFoundError:
    pass