# in dictionary while using multiple values we can use this format:

mydic={
    "brans" :"BMW",
    "model":"aspire",
    "year":[2018,2010],
    "color":["red","green","blue"],
}
print(mydic)

# Approach__2
#for when we are using single values for each:
mydic={ "brans" :"BMW","model":"aspire","year":2018,}
print(mydic)

# using dict()constructor
mydic=dict(name="john",age=35,country="USA")
print(mydic)

# a key can have multiple values:
mydic={
     "brans" :"BMW",
     "model":"aspire",
     "year":2018,
     "color":["red","green","blue"],
}
print(mydic)

#Accessing items from the dictionary
# its notting but printing the particular value
# you can access the items of a dictionary by referring to its key name ,inside [] brackets:
# Approach_1
mydic={ "brand" :"BMW","model":"aspire","year":2018,}
print(mydic["model"])    #aspire

# Approach_2 : using the get() method
print(mydic.get("year"))   #2018

# Approach_2 : using the get() method
print(mydic.get("brand"))  #BMW

# method__1 by using keys() will return only the key names in the dictionary
mydic={"name":"john","age":35,"country":"USA"}
print(mydic.keys())   # dict_keys(['name', 'age', 'country'])


#  method__2  by using values() it will return the only values of the names in the dictionary
mydic={"name":"john","age":35,"country":"USA"}
print(mydic.values())  #dict_values(['john', 35, 'USA'])

# in casse if the user orders multiple brands in single order
#  it  will replace with the new values of the particular key instead of only key ,
#  because of dictionary won't allow duplicates values
mydic={
     "brand" :"BMW",
    "model":"aspire",
    "year":2018,
    "color":["red","green","blue"],
    "brand": "KTM",

}
print(mydic)

#  method__3   get items: items() method will return each item in a dictionary , as a tuple in a list

mydic={ "brands" :"BMW","model":"aspire","year":2018,}
print(mydic.items())
# print(mydic.keys())
# print(mydic.values())

# check if the key is exists (searching keys in the dictionary)
mydic={ "brands" :"BMW","model":"aspire","year": "2018",}

if "mohan" in mydic:
    print("model exists:-----------------")
else:
    print("model does not exist:------------------")

if "BMW" in mydic:   # values we cannot exists only keys
    print("BMW exists")
else:
    print("BMW does not exist")

# adding items in the dictionary

mydic={ "brands" :"BMW","model":"aspire","year": "2018",}
mydic["color"]=["red","green","blue"]
print("before updating the dic: ",mydic)

mydic={ "brands" :"BMW","model":"aspire","year": "2018",}
mydic.update({"brands":"KTM","model":"aspire","year":"208"}) #in the place of BMW, Updating to KTM
print("After updating the dic: ",mydic)

# removing items in the dictionary

# approach_1 pop()--

mydic={ "brands" :"BMW","model":"aspire","year": "2018",}
mydic.pop("brands")
print("After removing  the dic: ",mydic)  # by using keys we are removing

# approach_2:  using popitem()
mydic={ "brands" :"BMW","model":"aspire","year": "2018",}
mydic.popitem()
print("After Poping  the dic: ",mydic) # here it will remove with out passing the key but last values it removes

# approach__3  by using DEL keyword --removing item from the dictionary

mydic={ "brands" :"BMW","model":"aspire","year": "2018",}
del mydic["model"]
# del mydic  # NameError: name 'mydic' is not defined
print("After deleting  the dic: ",mydic)

# approach__3  by using clear() keyword --removing item from the dictionary
mydic={ "brands" :"BMW","model":"aspire","year": "2018",}
mydic.clear()
print("After clearing the dic: ",mydic)
mydic["color"]="red"
print("After updating the dic: ",mydic)

# copying COPY() dic form one dic to another dic
mydic1={ "brands" :"BMW","model":"aspire","year": "2018",}
mydic2=mydic1.copy()
print("Copying from dic-1:",mydic2)

# method_2
mydic1={ "brands" :"BMW","model":"aspire","year": "2018",}
mydic2=dict(mydic1)
print("Copying from dic2:",mydic2)


mydic={ "brands" :"BMW","model":"aspire","year": "2018",}
mydic["salary"]=1000,5555,666
print("after updating the values: ",mydic)

mydic.pop("salary")
print("after removing the values: ",mydic)

mydic.pop("brands")
print("after removing the values: ",mydic)

if "salary" in mydic:
    print("salary exists")
else:
    print("salary does not exist")

if"brands" in mydic:
    print("brands exists")
else:
    print("brands does not exist")



# coping from one dict to another dict
# approach_1 copy()
mydic1={ "brands" :"BMW","model":"aspire","year":2018,}
mydic2=mydic1.copy()

print(mydic1)
print(mydic2)

# approach_2 copy()
mydic1={ "brands" :"BMW","model":"aspire","year":2018,}
mydic2=dict(mydic1)

print(mydic1)
print(mydic2)

# length of the dictionary
mydic1={ "brands" :"BMW","model":"aspire","year":2018,}
print(len(mydic1))

# looping with dictionary
mydic1={ "brands" :"BMW","model":"aspire","year":2018,}

# req:Printing all the keys names in the dictionary, one by one
for x in mydic1.keys():
    print(x)
# req:Printing all the values names in the dictionary, one by one
for x in mydic1.values():
    print(x)
# req:Printing all the keys and values names in the dictionary, one by one
for x,y in mydic1.items():
    print(x,y)


