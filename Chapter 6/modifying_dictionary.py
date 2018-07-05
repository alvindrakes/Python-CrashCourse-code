# modifying value in dictionary 

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print('Original x_position: ' + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # must be a fast alien 
    x_increment = 3


# changing the x_position by adding x_increment 
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('The new x_position is: ' + str(alien_0['x_position']))

#--------------------------------------------------------------------------
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # must be a fast alien 
    x_increment = 3


# changing the x_position by adding x_increment 
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('The new x_position is: ' + str(alien_0['x_position']))

