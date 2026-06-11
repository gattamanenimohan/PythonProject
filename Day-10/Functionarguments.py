# Arbitrary or variable length arguments
# positional or required arguments
# key arguments


# example-1  function with Arbitrary arguments
# "n" number of arguments receiving in a one single tuple represent "*"

# def myfun(*numbers):   # variable length arguments are also we can called
#     total = 0
#     for i in numbers:
#         total=total+i
#     return total
# print(myfun(1,2,3,4,5,6))
# print(myfun(1,2,3,4,5,6))
# print(myfun(1,2,3,4,5,6))
#
# # method_2
# def myfun(a,b,c,d):
#     return a+b+c+d
# print(myfun(3,2,3,3))
# print(myfun(1,2,3,4))


# # example_2 functional with positional and keyword arguments
# def myfunc(i,j,k):
#     print(i,j,k)
# myfunc(1,2,5) # positional arguments
# myfunc(j=1,k=2,i=2) # keyword arguments
#
# # example_3 default values can be assigned to the positional arguments
# def myfunc(i=1,j=2,k=10):
#     print(i,j,k)
# myfunc(100)
# myfunc()

# example_4 mixing of both the positional and keyword arguments

def myfun(a,b,c):
    print(a,b,c)
myfun(10,30,40)  #positional arguments

myfun(b=30,a=10,c=40)  #keyword arguments
# myfun(30,10,b=40) # myfun() got multiple values for argument 'b'

# myfun(10,b=20,30)  # positional arguments should come before the key arguments

#example_5: functional can return multiple values

def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(largest(a=10,b=30))

res=largest(a=10,b=30)
print(res)
print(type(res))