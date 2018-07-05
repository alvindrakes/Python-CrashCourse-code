# dictionaries (just like structure in c programming)

alien_0 = {'colour':'green', 'point': 5}     # dictionaries in python is a 
                                            # collection of key-value pairs

print(alien_0['colour'])               # colour is the key
print(alien_0['point'])                # green is the value 

new_points = alien_0['point']
print('You have earned a new ' + str(new_points) + ' points.\n')

print(alien_0)

alien_0['x_position'] = 0     # python doesn't care about the orders in 
                              # dictionaries, it only care about the connection
                              # between the key and the value 
alien_0['Y_position'] = 25
print(alien_0)