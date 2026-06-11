# importing functions form one module to another
#approach_1:
import Operations

# Operations.add(1,5,5)
# Operations.mult(2,5)
# print(Operations.person["age"])
# print(Operations.person["name"])


#approach_2: if you having multiple functions but you need to import  few, by the time we need to use this
# if you are not importing  and  calling that function/calss meams will get errot

# from Operations import add,mult
# add(11,22,40)
# mult(3,5)
# # print(person["country"])    # error  name 'person' is not defined


#Approach_3:
from Operations import * # means it can call every thing in the module
add(11,22,40)
mult(3,5)
print(person["country"])