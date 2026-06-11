# example_1
from itertools import repeat

# print("hell"  # causing the error

# example_2: exception
# n=10
# res=n/0
# print(res)  # ZeroDivisionError: division by zero
# example_3:
# x='10'
# x=int("10")
# print(x)

# example_4: handling exception "try & except"

# # error
# print("exception is started")
# print(x)  #it will through an 'ERROR' and rest of the code not going to print
# print("exception si ended")

# in exception method
#  because if hte try & except it will hold that particular position and it will run the remaining code
# print("exception  is started")
# try:
#     print(moahn)
# except:
#     print("exception is occured")
# print("exception is ended")

# example: many exception(we can define multiple exceptions in single try

# try:
#     print(x)
# except NameError:
#     print("variable x is not defined")
# except:
#     print("something is wrong")


# example: using the try: & except: & else:
# we can use the else keyword to define the block of code to be executed if no errors ware raised
# try:
#     print("mohan")
# except:
#     print("something went wrong")  # if any issues only except will print/no issues try/else will print
# else:
#     print("notting went wrong")

# example: Finally
# finally keyword is executed even though try block is raises an error or not   no matter
# if anything is wrong except,finally will print if not try and finally
# try:
#      print("mohan")
#     # print(mohan)
# except:
#     print("something went wrong")
# finally:
#     print("finally executed ")


# example_8: try, except, else, finally
#
try:
    n=int(input("Enter a number: "))
    res=100/n

except ZeroDivisionError:
    print("you cannot divide by 0")
except ValueError:
      print("enter valid number")
else:
     print(res)
finally:
    print("finally exception is completed")


# example_9 : try inside the try block
#
# try:
#     a=int(input("enter the name  of a: "))
#     try:
#         print("user entered name successfully")
#     except:
#         print("enter valid data")
#     finally:
#         print("finally closing the exception ")
# except:
#     print("user entered invalid data")
