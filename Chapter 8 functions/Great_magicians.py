# 8.10 great magicians

magician_names = ["Alvin", "drakes", "Elvis", "Kon"]


def show_magicians(magician_names):
    for name in magician_names:
        print("Hello I am a magician, my name is " + name.title() + " :D")


def make_great(magician_names):
    for i in range(len(magician_names)):   #use index to change individual element in the list
        magician_names[i] += "the GREAT"
      
    



make_great(magician_names)
show_magicians(magician_names)


