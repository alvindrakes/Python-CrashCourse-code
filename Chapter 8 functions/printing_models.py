""" 
#start with some design that needs to be printed
unprinted_designs = ["iphone cases", "robot pendant", "tesla model S"]
completed_models = []

# simulate printing design until there's non left
# move each done models to completed models 
while  unprinted_designs:
    current_design = unprinted_designs.pop()

# simulate creating
    print("Printing Model: " + current_design)
    completed_models.append(current_design)

# dislay all completed models
print("\nAll completed models: ")
for models in completed_models:
    print(models) 
"""

# more efficient of doing teh above programs is by creating functions
def print_models(uncomplete_models, completed_models):

      while uncomplete_models:
        current_design = uncomplete_models.pop()
        print("Printing Model: " + current_design)
        completed_models.append(current_design)

def show_completedModels(completed_models):
    print("\nAll completed models: ")
    for models in completed_models:
        print(models)

uncomplete_models = ["Tesla model S", "Iphone 8", "real estate 7"]
completed_models = []

print_models(uncomplete_models[:], completed_models)  # the [:] symbol create a copy of list and send 
# that to the function, so the original list will not be modified
show_completedModels(completed_models)

    

      


