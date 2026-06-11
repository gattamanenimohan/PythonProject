# example_1: creating a class along with object
# class is a blue print to create 'n' number of objects

class Myclass:   # class name
    def myfun(self,):
        pass
    def display(self,name):
        print(name)

mc1=Myclass()   #objects-1   #mc1 is an object (instance) of Myclass.
mc1.myfun()
mc1.display("hello")

mc2=Myclass()   #objects-2  #mc2 is another separate object of the same class.
mc1.myfun()
mc1.display("scott")


# example_2  : instance vs static methods

#  self is representing as a class
# in static method self is representing as variable name
# A static method in Python does not take the instance (self) or class (cls) automatically as the first argument.
# It behaves like a normal function but lives inside the class namespace.

class Myclass:
    def m1(self,name):
        print("this is instance method....")

    @staticmethod
    def m2(self,num):
        print(self,num)

mc=Myclass()  #object creation
mc.m1()
mc.m2(10,20)
print("----------")

# example_3 define the variables inside the class--(class variable/instance variable)
# global variable----out side of the  function we can use
# local variable-----insdie of the function we can use

# x=10
# def myfun():
#     x=120
#     y=200
#     print(x,y)
# myfun()
# print(x)

class Myclass: # self. is must when calling the class variable in to the  local variable
    a,b=10,20

    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

mc=Myclass()
mc.add()
mc.mul()

print("--------------")

# example_4: local variable -and- global variable -&- class variable

i,j=15,30  # global variable

class Myclass:
    a,b=10,20  #class variable

    def add(self,x,y):
        print(x+y)   #local variable ---/-----we can access  directly
        print(self.a+self.b) # class varialbe---/------by using self keyword we can use class variable
        print(i+j)   # global variable---/------ we can access directly

gmk=Myclass()
gmk.add(100,200)  #values belongs to local variable
print("--------------")

# example_5:  local variable -and- global variable -&- class variable (names of the variable are same)
a,b=15,30  # global variable

class Myclass:
    a,b=10,20  #class variable

    def add(self,a,b):
        print(a+b)   #local variable ---/-----we can access  directly
        print(self.a+self.b) # class variable---/------by using self keyword we can use class variable
        print(globals()['a']+globals()['b'])   # global variable---/------ we can access directly

gmk=Myclass()
gmk.add(10,20)
print("--------------")

# example_6 class with constructor
# --init__(self)   : constructor
# invoked automatically when object is created
class Myclass:
    def __init__(self):
        print("this is constructor.....")
    def m1(self):
         print("this is m1.....")
    def m2(self,x,y):
         print(x,y)

mc=Myclass()
mc.m1()
mc.m2(1,1)
print("--------------")

#example_7: constructor with parameters and class variable

class Myclass:
    name="mohan"        # class variable
    def __init__(self,name):
        print(name)           #local variable
        print(self.name)      # class variable


mohan=Myclass("hello")
print("--------------")

# example8_ A class with constructor and method
class emp:
    def __init__(self,eid,sal,ename):
        self.eid=eid   #class variable
        self.sal=sal   #class variable
        self.ename = ename  #class variable

    def display(self):     #method-------
        print(self.eid,self.sal,self.ename)


gmk1=emp(200,10,"mohan")   # objects
gmk1.display()
gmk2=emp(201,1222,"mohan")
gmk2.display()

# for example
class Myclass:
    a,b=10,20
    def __init__(self,a,b):
        print(a,b)
        print(self.a+self.b)
    def firstname(self,name,lastname,mobile):
        print(self.a,self.b,name)
        print("my first name is : ", name,lastname,mobile)
    def lastname(self,lastname):
        print("my last name is: ", lastname)
    def mobile(self,mobile):
        print("my mobile number is: ", mobile)

gmk=Myclass(a,b)
gmk.firstname("mohan","gmk",456789)
gmk.lastname("krishna")
gmk.mobile(1045678920)


# examples----------------------
x,y=12,13
class Myclass:
    a,b=20,30
    def __init__(self,a,b):
        print(a,b)      #loccal variable
        print(self.a+self.b)    #class variable
        global x  # changing the value of global variable 'X'
        x = 2000
        print(x)
        print(globals()['x'],globals()['y'])  # global variable
        print("subtracting the variable:  ",globals()['x']-globals()['y'])  # global variable
        print("adding the variable:  ",globals()['x']+globals()['y'])  # global variable
        print("multiplication the variable:  ",globals()['x']*globals()['y'])  # global variable


mc=Myclass(10,20)
print(x,y)




