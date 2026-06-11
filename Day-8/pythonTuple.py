from itertools import count

# creating the tuple:

mytuple=("mohan", "apple", "banana")
print(mytuple)

# Access tuple elements/values
mytuple=("mohan", "apple", "banana")
print(mytuple[-1])
print(mytuple[0])


# count number of time repeated
mytuple=("mohan","mohan","banana", "apple","banana","banana","apple")
print(mytuple.count("banana"))
print(mytuple.count("apple"))

# range of indexes
mytuple=("mohan","apple","banana","graphs","lemon","pineapple")
print(mytuple[-4:-1])

# chang the values in the tuple
# by default tuple we cannot change the values bcoz it is immutable
# there is workaround by changing as a tuple to list then we can chang the values
# duplicates allowed

# tuple--->list---->tuple

mytuple=("mohan","apple","banana","graphs")
mylist=list(mytuple)
print("after converting in to the list: ",mylist)
mylist[2]="king"
print("after changing mylist ",mylist)
mytuple=tuple(mylist)
print(mytuple)

# method _2
mytuple=("1","2","4","6","7")
mylist=list(mytuple)
print("changing into the list: ",mylist)
mylist[2]="222222222"
print("after changing my list:",mylist)
mytuple=tuple(mylist)
print(mytuple)

# method_3
mytuple=("firstname","lastname","age")
print(mytuple)
mylist=list(mytuple)
print("before changing the list",mylist)
mylist[2]="email"
print("after changing the value form the list: ",mylist)
mytuple=tuple(mylist)
print(mytuple)
print("-----------------------------------------------------")


#retrive the data from tuple by using looping statement like one by one

mytuple=("firstname","lastname","age")
for i in mytuple:
    print(i)

# search in an item i a tuple
mytuple=("firstname","lastname","age")

if "age" in mytuple:
    print("is present")
else:
    print("is not present")

# length or count number of values in a tuple
mytuple=("firstname","lastname","age")
print(len(mytuple))

# adding two different  tuple to another one  tuple
mytuple1=("firstname","lastname","age")
mytuple2=("password","email","mobile number")
print(mytuple1)
print(mytuple2)
mytuple3=mytuple1+mytuple2
print(mytuple3)

# coping one tuple to another
mytuple1=("firstname","lastname","age")
mytuple2=mytuple1

print(mytuple2)

# removing the values from the tuple is not possible bcz tuple is immutable
# mytuple=("firstname","lastname","age")
# mytuple.remove("age")
# print(mytuple)    # you will get error

# for example try to change tuple to list----------------

mytuple=("company name","brand","logo","destination")
mylist=list(mytuple)
print("Before changing the values in  tuple to list : ", mylist)
mylist.append("joining data")  #it will add in last
mylist[2]=("joining data")
print("after changing the values in  list via tuple: ",mylist)
mytuple=tuple(mylist)
print(mytuple)


# pop() : removes a random item /values fom the set
myset={"banana","cherry","mango"}
myset.pop()
print("after removing  by using POP: ",myset)



# changing the values in the form of tuple to list

mytuple = ("mohan", "apple", "banana", "krishna", "qualitest")

print("original data before converting :",mytuple)
mylist = list(mytuple)
print("after converting into the list : ", mylist)
mylist[2]=("sweet")
mytuple=tuple(mylist)
print("after converting back to the tuple  : ",mytuple)


