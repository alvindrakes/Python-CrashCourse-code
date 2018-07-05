# changing guest list 

guest = ['father', 'mother', 'brother', 'sister']
print ("Hello " + guest[0].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[1].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[2].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[3].title() + ", I would like to invite you to my dinner party.\n")


guest_cannot_make_it = ['father', 'mother']

guest[0] = 'aunt'
guest[1] = 'uncle'
print (guest_cannot_make_it[0].title() + " and " + guest_cannot_make_it[1] + " can't attend the party.")
print ("Hello " + guest[0].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[1].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[2].title() + ", I would like to invite you to my dinner party.")
print ("Hello " + guest[3].title() + ", I would like to invite you to my dinner party.")



