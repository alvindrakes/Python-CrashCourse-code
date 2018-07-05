# store info about a pizza being oddered

pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
    }

#summarize the order
print("Your ordered a " + pizza['crust'] + "-crust pizza " + 
    "with the following topings:" )

for topping in pizza['toppings']:
    print("\t" + topping)
