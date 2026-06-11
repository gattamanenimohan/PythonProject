# we can store all types of data values
# unordered(so items will stored in random order)
#index is not supported
# duplicates not allowed
# represent with {} flower brackets
from itertools import count

# creating  set {}
myset1={10,20,30,40, 50,60}
myset2={4,5,6}
myset3={"apple","banana","mango"}
myset4=set(myset1) # coping same values for set-4 as set-1

print(myset1)
print(myset2)
print(myset3)
print(myset4)

# Access the values from a set
# we cannot access items in a set by referring to an index (bcoz set won't support index)
# we cannot change the values, but we can add new tems to set.
# access data from set using for loop

myset={"apple","banana","mango"}

for i in myset:
    print(i)

# searchin the values in the set
myset={"apple","banana","mango"}

if "apple" in myset:
    print("available")
else:
    print("not available")

# find length/number of values in a set
myset={"apple","apple","banana","mango"}
print(len(myset))
#print(count("apple"))

# count the values in the set is not possible
# since set is not allowed duplicates

# sorting the set
# means first to last
# - not possible, since set is unordered

# reversing the set
# - not possible, since set is unordered

# Add items /values into set
# add()    -we can add single value
# update() - we can add multiple values , since it will add randomly

myset={"banana","cherry","mango"}

# myset.add("mohan")
# print("after adding :",myset)
myset.update(["apple","guava","graphs"])
print(myset)

# remove items/ values from a set : remove, --Discard,
myset={"banana","cherry","mango"}
#myset.remove("rtyui") # it will through an error if the value is not in the set
myset.remove("banana")
print("after removing : ",myset)

myset={"banana","cherry","mango"}
myset.discard("XYZ") # it will not through any error if the value is not exists in the set
print("after removing : ",myset)

# pop() : removes a random item /values fom the set
myset={"banana","cherry","mango"}
myset.pop()
print("after removing  by using POP: ",myset)

# clearing values in the set
myset={"banana","cherry","mango"}
myset.clear()
print("after clearing  : ",myset)

# copying set
# approach_1---------
myset1={"banana","cherry","mango"}
myset2=set(myset1)
print(myset1)
print(myset2)

# approach_2------------
# myset1={"banana","cherry","mango"}
# myset2=myset1.copy()
# print(myset1)
# print(myset2)

# joining of multiple sets:
#  Approach_1---------using union()

myset1={"banana","cherry","mango"}
myset2={10,20,30,40,50}
myset3=myset1.union(myset2)
print(myset3)

# Approach_2----------
myset1={"banana","cherry","mango"}
myset2={10,50}
myset3=myset1 | myset2
print(myset3)

# retreving/identifying  common values form 2 sets:
# intersection()   &

# Approach_1------------
myset1={"banana","cherry","mango",10,"a"}
myset2={10,20,30,40,50,"a"}

myset3=myset1.intersection(myset2)
print(myset3)

# Approach_2------------
myset1={"banana","cherry","mango",10,"a"}
myset2={10,20,30,40,50,"a"}

myset3=myset1 & myset2
print(myset3)


mylist=[1,2,3,4,5,]
mylist.reverse()
print(mylist)