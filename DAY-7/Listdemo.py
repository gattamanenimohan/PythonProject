import is_palindrome
import palindrome
from PIL.EpsImagePlugin import split

mylist1=[10,20,30]
mylist2=["apple","banana","mango"]
mylist3=[10,"apple","A",True]
mylist4=mylist1+mylist2

print(mylist1)
print(mylist2)
print(mylist3)
print(mylist4)

# access- items/objects/values
mylist=["banana","apple","mohan","A"]
mylist7=()
# printing in positive values
print(mylist[1])
print(mylist[2])

print("my list 7: ",mylist7)

# printing in negative values
print(mylist[-1])
print(mylist[-4])

# Access multiple values from a list (range of indexes)
mylist=["apple","banana","cherry","orange","kivi","melon","mango"]
print(mylist[2:5])
print(mylist[:2])
print(mylist[:])
print(mylist[-4:-1])

# change the value  in List
mylist=["mango","apple","banana"]
print("Before changing :" ,mylist)
mylist[1]="mohan"
mylist[2]="pineapple"
print("after changing :", mylist)


# loop with list, means it will print one by one
mylist=["mango","apple","banana"]
for i in mylist:
    print(i)
print("--------------------------------------------------------")

#searching an item in the list
mylist=["mango","apple","banana"]
if "banana" in mylist:
    print("yes it is available in mylist")
else:
    print("not available in mylist")
print("--------------------------------------------------------")
# length of the list
mylist=["mango","apple","banana"]
print(len(mylist))

# length of the string, means it will count the character of the string
a="mohan"
print(len(a))
print("--------------------------------------------------------")

# count number of time the value is repeated in the list
mylist=["mango","apple","banana", "mango","apple"]
print(mylist.count("mango"))
print("--------------------------------------------------------")

# sorting the list
mylist=["banana","apple","cherry","mango"]
print("Before sorting:",mylist)
mylist.sort(reverse=True)  # it will give the elements in descending order
print("After sorting : " ,mylist)
print("--------------------------------------------------------")
# reversing the list of items

mylist=["Apple","banana","cherry","mango"]
mylist.append("guava") # append values will get added in end of the list
mylist.insert(1,"mohan") # insert means we can able to add in particular position
print("Original Values:",mylist)
mylist.reverse()
print("Reversed Values: " ,mylist)
print("--------------------------------------------------------")

# Removing---- the elements in the given list   ---pop---    and -----delete----

mylist=["apple","mango","mohan","krishna"]
print(mylist)
mylist.remove("mohan") # we need to specify the string which we need to remove
print("after removing  from te given list: ",mylist)
print("--------------------------------------------------------")
#by using the pop method we need to use index method to remove the value
mylist=["apple","mango","mohan","krishna"]
mylist.pop(1)
print("after pop from the given list: ",mylist)


# by using the remove method
mylist=["apple","mango","mohan","krishna"]
del mylist[0:2] # we passed index of the element , here del is not a method, it is a identifier/keyword
print("after deleting from te given list: ",mylist)

# deleting the entire list
# mylist=["apple","mango","mohan","krishna"]
# del mylist
# print(mylist)   #for this we can get the name error.
print("--------------------------------------------------------")
# coping from one list to another
# approach_1
mylist1=["apple","mango","mohan","krishna"]
mylist2=mylist1.copy()
print(mylist1)
print(mylist2)

# Approach_2
mylist1=["apple","mango","mohan","krishna"]
mylist2=list(mylist1)
print(mylist1)
print(mylist2)

print("--------------------------------------------------------")
# joining 2 different list into  one list
# method_1
mylist1=["apple","mango","mohan","krishna"]
mylist2=["mahesh", "babu"]
mylist3=mylist1+mylist2
print(mylist3)

# method_2
mylist1=['a' ,'b',' c']
mylist2=['12','4567','222']

for i in mylist2:
    mylist1.append(i)
print(mylist1)

# method _3
mylist1=['a' ,'b',' c']
mylist2=['12','2','222']

mylist1.extend(mylist2)
print(mylist1)

a="mohan"
reversed_a=a[::-1]
print(reversed_a)


b="king"

reversed_string= b[::-1]
print(reversed_string)



# Approach_2
mylist1=["apple","mango","mohan","krishna"]
mylist2=list(mylist1)
print(mylist1)
print(mylist2)






