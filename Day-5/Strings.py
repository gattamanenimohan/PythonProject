#  Creating strings in 3 Approaches:

# Approach:1 using double quotes
name="mohan"
grade="A"
print(name)
print(grade)

# approach -2 using single quotes:

name='mohan krishna'
grade ='A'
print(name)
print(grade)

# Approach-3: using constructor

name=str("mohan")
grade=str("A")

print(name,grade)

print(type(name))


#  + and * operators with strings.

str="welcome"

print(str+ " programming")
print(str* 5)

# formatting string:
# F - String was introduced in python 3.6 and is now preferred way of formatting strings.
# to specify a string as an f- string,
# simply put an "f" in front of the string literal, and add curl brackets {} as placeholder for the variables and other operations.

age=25
name1="mohan"
name2="krishna"
str= f"my name is {name1}, and my age : {age}"
print(str)

print(f"my name is {name2}, and my age {age}")


first_name="mohan"
second_name="chowdary"
total_marks= 30

str_1= f"myfirst name is {first_name}"
str_2=f"my second name is {second_name}"
str_3=f"my total marks is {total_marks}"

print(str_1, " ,  " , str_2, "  , " ,  str_3)




#
#
#
# price=30
# str=f"the price of the candle is {price:.3f}"
# print(str)
#
# # example-3:
price=20
str=f"the price of the movie ticket is {price *20}"
print(str)
#
price=500
str=f"this is my early salary {price * 12:.4f}" #2f notting but floating values after value .00
print(str)

# in not in with strings
# return the boolean value

str="india"
print("ind" in str)
print("id" in str)

print("ind" not in str)
print("id" not in str)

