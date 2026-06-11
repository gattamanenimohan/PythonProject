# mutable v/s immutable
# mutable= we can change the data after the creation
#   for ;list, dic, set's
#  immutable= we cannot change the data after the creation of data
#  for EX: int, float, tuple, str


s1="mohan"
print("original strings: ", s1)
print("address: ",id(s1))
# print(s1.replace("mohan","Mohan"))

s1="M000"+s1[1:]
print(s1)

# example-3
# mutable we can able to modify directly in list but we cant able to modify in string
mylist=["h","e","l","l","o"]
print("before modification: ", (mylist))
mylist[0]="MOHAN"
mylist[4]="krishna"
print("after modification: ", (mylist))