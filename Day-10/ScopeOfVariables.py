# global variables: variables which we are creating out of the function is called global
# local variables:  variables which we are creating in side of the function is called local

# example_1
x=20  # global variable we can use evey where
def myfun():
    y=10  #local variable
    print(x) # able to access global variable with in the function
    print(y)
myfun()

print(x)
#print(y)  #you will get type error because it is local variable

print("______________________")
# example_2
x=200
def myfun():
    x=10
    print(x)  #  now it will consider local variable
myfun()
print(x) # now it will consider global variable

print("______________________")

# example_3 if user want to modify global variable
x=200
def myfun():
    # global x    # we are modifying the global variable in local variable
    x=10
    print(x)  # 10
myfun()

print(x) #200
print("______________________")
# example_4 : declare the global variable inside the local variable
def myfun():
    global x
    x=20
    print(x)
myfun()
print(x)



