# more guests


guest = ['father', 'mother', 'brother', 'sister']
print ("Hello " + guest[0].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[1].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[2].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[3].title() + ", I would like to invite you to my dinner party.\n")


guest_cannot_make_it = ['father', 'mother']                # guests that can't make it to the party

guest[0] = 'aunt'                          # change value in list 
guest[1] = 'uncle'

print (guest_cannot_make_it[0].title() + " and " + guest_cannot_make_it[1] + " can't attend the party.")
print ("Hello " + guest[0].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[1].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[2].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[3].title() + ", I would like to invite you to my dinner party.\n")

print ("Apparently I have found a bigger dining table, I can invite more poeple now!")

guest.insert(0, 'cousin')
guest.insert(3, 'Jaden')                 # add more value in list 
guest.append('kon')

print ("Hello " + guest[0].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[1].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[2].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[3].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[4].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[5].title() + ", I would like to invite you to my dinner party.\n")





