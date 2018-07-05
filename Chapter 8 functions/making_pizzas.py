"""
import pizza3  #import function from another module

pizza3.make_pizza(6, "Mushroom")
pizza3.make_pizza(8, "peperoni", "Chilli", "pepper")

# to use the function in another module, just type
# module_name.function_name()
"""

from pizza3 import make_pizza  # this import only specific function

make_pizza(6, "Mushroom")
make_pizza(8, "peperoni", "Chilli", "pepper")

