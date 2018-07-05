# 8.11 unchanged magicians

magician_names = ["Alvin", "drakes", "Elvis", "Kon"]
new_list = []


def show_magicians(magician_names):
    for name in magician_names:
        print("Hello I am a magician, my name is " + name.title() + " :D")


def make_great(magician_names):
    for i in range(len(magician_names)):   #use index to change individual element in the list
        magician_names[i] += "the GREAT"
        new_list.append(magician_names[i])
      
    



make_great(magician_names[:])
show_magicians(magician_names) #unmodified name list
show_magicians(new_list)  #modified names list


