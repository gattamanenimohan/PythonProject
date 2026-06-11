from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# to open multiple windows

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.example.com")
# driver.implicitly_wait(10000)
#
# # Open a new window (example)
# driver.execute_script("window.open('https://www.google.com');")
#
# # Open a new window-2 (example)
# driver.execute_script("window.open('https://www.amazon.com');")
#
# # Get all window handles
# windows = driver.window_handles
# print(windows)
#
# # Switch to the new window
# driver.switch_to.window(windows[1])
# print("Now in Google window:", driver.title)
#
# # Switch to the new window
# driver.switch_to.window(windows[2])
# print("Now in Google window:", driver.title)
#
# # Switch back to original window
# driver.switch_to.window(windows[0])
# print("Back to original window:", driver.title)





# def is_palindrome(word):
#     return word == word[::-1]
# # Examples
# print(is_palindrome("madam"))   # True
# print(is_palindrome("racecar")) # True
# print(is_palindrome("hello"))   # False
# print(is_palindrome("121"))     # True
# print(is_palindrome("123"))     # False
#
#
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
#
#
# # Take input from user
# num = int(input("Enter the number of terms: "))
# fibonacci(num)
#
#
# # Example: First 10 Fibonacci numbers
# fibonacci(10)




# changing the tuple in to the list
# mytuple=("company name","brand","logo","destination")
# mylist=list(mytuple)
# print("Before changing the values in  tuple to list : ", mylist)
# mylist.append("joining data")  #it will add in last
# # mylist[2]=("joining data")
# print("after changing the values in  list via tuple: ",mylist)
# mytuple=tuple(mylist)
# print(mytuple)

# changing the values from tuple to list.
mytuple=("my name is mohan", "iam form tirupathi")
print("printing the values in the tuple format only",mytuple)
mylist=list(mytuple)
print("before changing the values in the tuple",mylist)
mylist.append("new value")
print("after changing hte values in the tuple",mylist)
mytuple=tuple(mylist)
print(mytuple)


# changing the values in the form of tuple to list

mytuple = ("mohan", "apple", "banana", "krishna", "qualitest")
print("original data before converting :",mytuple)
mylist = list(mytuple)
print("after converting into the list : ", mylist)
mylist[2]=("mango")
mytuple=tuple(mylist)
print("after converting back to the tuple  : ",mytuple)


