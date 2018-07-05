# give the function name in another module a nickname(alias)
"""
from pizza3 import make_pizza as mp

mp(6, "Mushroom")
mp(8, "peperoni", "Chilli", "pepper")
"""

# we can also give the module an alias

import pizza3 as p

p.make_pizza(6, "Mushroom")
p.make_pizza(8, "peperoni", "Chilli", "pepper")