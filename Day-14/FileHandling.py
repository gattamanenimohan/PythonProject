# example_1  : create /writing new file
import shutil

# approach_1
file=open("C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\myfile.txt",'w')
file.write("Hello World")
file.close()

# approach_2: by using with
with open("C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\myfile_1.txt",'w')as file:
    file.write("Hello World, iam in india")
    file.close()



# appending data into the existing file
# Example_2:---

# approach_1
file=open("C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\myfile.txt",'a')
file.write("\n my name is mohan krishan")
file.close()

# approach_2: by using with
with open("C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\myfile_1.txt",'a')as file:
    file.write("\n this is newly append line")
    file.close()


# example_3: reading data from text files
# read() - read entire data
# readline() - it will single line form the data
# readlines() -- read all the lines in the list format
file=open("C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\myfile_1.txt",'r')
# content=file.read()
# content=file.readline()
content=file.readlines()
print(content)
file.close()

# # renaming the file-------------------
# import os
# os.rename("C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\myfile_1.txt","C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\My filemydecision.txt")
# print("file renamed")

# # deleting the file----------------
# import os
# file="C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\myfile_1.txt"
# if os.path.exists(file):
#     os.remove(file)
# else:
#     print("file not exist")

# creating the directory /file----------
# import os
# os.mkdir("C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\mydir")
# print("directory is created")

# # checking the directory is exist or not----------------------

# import os
# mkdir= "C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\mydir"
#
# if os.path.exists(mkdir):
#     print("directory is exists")
# else:
#     print("directory is already exist")

# # renaming the directory------------------

# import os
# os.rename("C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\mydir","C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\New folder\\mydir_11")
# print("directory is renamed")

# removing the directory------------------

import os
os.rmdir("C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\GMK") # if the folder /directory is empty
print("directory is removed")
shutil.rmtree("C:\\Users\\320268735\\OneDrive - Philips\\mohan--personal\\GMK") # it will delete even though files contains
