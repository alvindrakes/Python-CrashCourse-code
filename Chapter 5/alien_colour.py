# 5.3 alien colour 

alien_colour = ['blue', 'green', 'yellow', 'red']

alien = 'green'
alien2 = 'red'

if alien in alien_colour:
    print('You have earned 5 points')

if alien2 in alien_colour:
    print('You got yourself a bonus point!\n')
elif alien2 not in alien_colour:
    print('You hit the wrong target')


# 5.4 alien colour 2.0 

if alien in alien_colour:
    print('You have earned 5 points')
else:
    print('You have earned 10 points')

if alien in alien_colour:
    print('You got yourself a bonus point!\n')
elif alien not in alien_colour:
    print('You hit the wrong target')