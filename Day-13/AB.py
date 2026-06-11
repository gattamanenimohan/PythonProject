# # Approach_1
# import a
# import B
#
#
# aobj=a.Animal()  # for cass this Aobj Is mandatory because with out object can't access and  print out put
# aobj.display()
#
# Bobj=B.Bird()
# Bobj.display()

# Approach_2

from a import Animal  # if you want only few
from B import Bird
# from a import *   # if you want to call all the classes/functions.
# from B import *

aobj=Animal()
aobj.display()

Bobj=Bird()
Bobj.display()
