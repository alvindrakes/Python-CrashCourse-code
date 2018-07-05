# 10.1 learning Python
# using 3 ways to display the contents in the file

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

    print(python_lessons)
