# 10 .10 Common words

filename = 'astronomy.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
        Common_word = contents.lower().count('the')

    print("The amount of time 'the' appear in the text is " + str(Common_word))

except FileNotFoundError:
    pass