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