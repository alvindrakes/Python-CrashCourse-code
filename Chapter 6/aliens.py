# nesting in dictionaries

aliens = []

#make 30 aliens
for aliens_number in range(30):
    new_alien = {'colour': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# change first 3 alien attributes 
for alien in aliens[0:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = '10'
    elif alien['colour'] == 'red':
        alien['colour'] = 'yellow'
        alien['speed'] = 'fast'
        alien['point'] = '10'


#show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("......")


print("Total number of aliens is " + str(len(aliens)))