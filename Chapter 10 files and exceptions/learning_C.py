# 10.2 learning C

filename = 'learning_python.txt'

with open(filename) as file_object:
 #   contents = file_object.read()

 #   print(contents)
 #   print("\n")

    python_lessons = ''

    contents = file_object.readlines()

    for content in contents:
 #      print(content)


        python_lessons += content


    modified = python_lessons.replace('Python', 'C') #need to save result to a variable
    
    print(modified)
