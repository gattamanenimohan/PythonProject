#
# example_1: NO parameter and NO return value

# creating the function
def myfunc():
    print("hello world")

myfunc()  # calling the function , and we can use multiple times


# Example 2: with parameter and No return values

def myfunc(name): # parameter can present inside the bracket "name" is parameter
    print("hello",name)

myfunc("mohan") # passing the argument
myfunc("krishna") # passing the argument

# if we need to check names are persent are not:
text="hello mohan"
if "hello" in text:
    print("exists: ",text)
else:
    print("not exists: ",text)

# Example 3: with parameter and   with return values
# method_1
def cal(a,b):
    return (a+b)
sum=cal(10,20)
print(sum)
print(cal("mohan","krishna"))


def adding_of_teo_numbers(a,b,c):
    return a+b+c
print(adding_of_teo_numbers(10,20,30))

# method_2
def add(items):
    return items
print(add("mango"))

# example-4 function return none

def myfun():
    i=100
    return i
print(myfun())

def myfun(int):
    return int
print(myfun(123.345))     # it will print none because we are not given any return value
