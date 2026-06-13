list= [10,20,30,20,20]

print(list)
print()
print(type(list))

from collections import Counter

lst = [10, 20, 30, 20, 20]
duplicates = [item for item, count in Counter(lst).items() if count > 1]
print("Duplicated values:", duplicates)

tup = (10, 20, 30, 20, 20)
duplicates = [item for item, count in Counter(tup).items() if count > 1]
print("Duplicated values:", duplicates)


lsit = [10, 20, 30, 20, 20, "mohan", "krishna", "mohan"]

duplicates = [i for i, count in Counter(lsit).items() if count >1]
print("Duplicated values:", duplicates)

# weapin teh upper and lower case

text = "My  self  is   mohan"
text = text.replace("m", "M", 1).replace("M", "m", 1)

# count → the maximum number of occurrences to replace, starting from the left.
# print(text.replace("m", "M", 1))  # replaces first 'm'
# print(text.replace("m", "M", 2))  # replaces first two 'm'
# print(text.replace("m", "M", 3))  # replaces first three 'm'
print(text)


