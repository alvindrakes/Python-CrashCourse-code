def print_models(uncomplete_models, completed_models):

      while uncomplete_models:
        current_design = uncomplete_models.pop()
        print("Printing Model: " + current_design)
        completed_models.append(current_design)

def show_completedModels(completed_models):
    print("\nAll completed models: ")
    for models in completed_models:
        print(models)