# 10 .8 cats and dogs 

filenames = ['cats.txt', 'dogs.txt']

try:
    for filename in filenames:
        with open(filename) as file_object:
            contents = file_object.read()

        print(contents)

except FileNotFoundError:
    print("The file that you are looking is not here.")