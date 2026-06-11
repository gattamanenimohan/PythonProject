# capitialize ()

a="mohan"
print(a.capitalize())

b="MOHAN KRISHNA"
print(b.lower())

C="mohan chowdary"
print(C.upper())

# title () it converts every first character in to upper case
c="my name is mohan"
print(c.title())

# swap case () it will become lower to upper case vise versa
d="My Favourite Color Is Blue"
print(d.swapcase())

d="mY fAVOURITE cOLOR iS bLUE"
print(d.swapcase())

# center() it will return in center
str="mohan"
print(str.center(15))

# format() formats specified values in a string
name ="john"
print("hello {}".format(name))

print("-------------")

# find() searches the strings for a specified value and returns the position of where it was found.
# in case if it having multiple it will take the first value only
a="mohan krishna"
print(a.find("h"))
print(a.find("n"))
print(a.find("c"))  # value is not found displayed as -1 o/p

print("-------------")
# index() searches the strings for a specified value and returns the position of where it was found.
# # in case if it having multiple it will take the first value only
a="mohan krishna"
print(a.index("h"))
print(a.index("n"))
# print(a.index("c"))  # value error : O/P

print("-------------")

# count() it will return the number of the specific value present in string
a="BANANA"
print(a.count("A"))
print(a.count("NA"))

print("-------------")

# replace() returns a string where a specified old value to new value

a=("hello india")
print(a.replace("india","mohan"))
print(a.replace("l","q"))

b=("my name is gmk, where my surname is 123")
print(b.replace("gmk","mohan"))
print(b.replace("123","krishna"))

print("-------------")
# isalnum() returns true if all the characters in the string are alpha numeric
a="abc123"
print(a.isalnum())
a="abc"
print(a.isalnum())
a="123"
print(a.isalnum())
a="abc!"
print(a.isalnum())

print("-------------")
# isalpha() returns true if all the characters in the string are in alphabet
a="abc123"
print(a.isalpha())
a="abc"
print(a.isalpha())
a="123"
print(a.isalpha())
a="abc!"
print(a.isalpha())
print("-------------")

# isdecimal()  returns true if all the characters are in decimal (0-9)
s="123"
print(s.isdecimal())
s="123.12"
print(s.isdecimal())


text = "Hello"
reversed_text = text[::-1]
print(reversed_text)  # Output: olleH

# method_2
a="mohan"
reversing_str = a[::-1]
print(reversing_str)



text = "Hello"
reversed_text = ''.join(reversed(text))
print(reversed_text)  # Output: olleH


text = "Hello"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print(reversed_text)  # Output: olleH


for i in range(10, 0, -2):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(0, 10, 1):
    print(i)

x="mohan"
x=x.upper()
# x=x.capitalize() nahoM
reverse=x[::-1]
print(reverse)



