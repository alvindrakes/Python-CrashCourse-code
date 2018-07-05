# list 

bicycles = ['trek', 'cannondale', 'redline', 'specialized']      #store different elements in a list 
print (bicycles)
print (bicycles[0])
print (bicycles[0].title())

print (bicycles[1])
print (bicycles[3])

print (bicycles[-1])    # use index -1 to access the last item in the list 
print (bicycles[-2])    # then -2 to access last second item and so on ...

message = "My first bicycle is a " + bicycles[0].title() + "."
print (message)