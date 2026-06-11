# import Pack1.Module1
# import Pack1.Pack2.Module2
# import Pack1.Module2
#
# Pack1.Module1.display()
# Pack1.Pack2.Module2.Show()
#
# Pack1.Module2.Show()

# Approach_2

# from Pack1 import Module1
# from Pack1.Pack2 import Module2
#
# Module1.display()
# Module2.Show()

# Approach_3

from Pack1.Module1 import *
from Pack1.Pack2.Module2 import *

display()
Show()