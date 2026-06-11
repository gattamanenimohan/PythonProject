#approach_1

# import Bird
# import Animal
#
# Animal.color()
# Animal.fly()
#
# Bird.color()
# Bird.fly()

# Approach_2
# during this importing using * it will print latest import one
#  to avoid this we need to call separately
from Bird import *
from Animal import *

fly()
color()
from Bird import *
fly()
color()