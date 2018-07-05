# birthday greting message 

age = 23

"""
message = "Happy " + age + "rd Birthday!"     

                                                 #this is considered as 'type' error because
                                                  python don't know whether to use numerical value 23 or character 2 and 3 

print (message)

"""


message = "Happy " + str(age) + "rd Birthday!"    # by using str(), we are telling python to use 23 as string of characters
print (message) 



