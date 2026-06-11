# multi level  Inheritance ---- like one parent and more than one  child class

# class A:   #parent class
#     def m1(self):
#         print("this is M1 method from class A")
#
# class B(A):   # child class
#     def m2(self):
#         print("this is M2 method from class B")
#
# class C(B):  # child class
#     def m3(self):
#         print("this is M3 method from class C")
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()
#
# # method _2
# # single level  Inheritance ---- like one parent and one  child class
#
# class A:
#      # a,b=10,20
#     def m1(self,a,b):
#         print(a+b)
#
# class B(A):
#     # x,y =200,100
#     def m2(self,x,y):
#         print(x - y)
#
# bobj=B()
# bobj.m1(10,20)
# bobj.m2(200,2)
#
# # method_3
# class A:
#      a,b=10,20
#      def m1(self):
#         print(self.a+self.b)
#
#
# class B(A):
#      x,y =200,100
#      def m2(self):
#         print(self.x - self.y)
#
#
# bobj = B()
# bobj.m1()
# bobj.m2()
# print("-----------------------")
#
# # Example_4- Heirachry inheritance
#
# class A:
#      a,b=10,20
#      def m1(self):
#         print(self.a+self.b)

# class B(A):
#      x,y =200,100
#      def m2(self):
#          print(self.x - self.y)
#
# class C(A):
#     i,j=10,20
#     def m3(self):
#         print(self.i * self.j)
#
# bobj = B()
# bobj.m1()
# bobj.m2()
#
# cobj=C()
# cobj.m1()
# cobj.m3()
# print("-----------------------")
# # MULTIPLE INHERITANCE
#
# class A:
#     a, b = 10, 20
#     def m1(self):
#         print(self.a + self.b)
#
# class B:
#     x, y = 200, 100
#     def m2(self):
#         print(self.x - self.y)
#
#
# class C(A,B):
#     i, j = 10, 20
#     def m3(self):
#         print(self.i * self.j)
#
# cobj=C()
# cobj.m1()
# cobj.m2()
# cobj.m3()
#
# # EXAMPLE_6  Calling parent class method using child cass (using super() )
# # invoke the parent class method and parent class variable from the child class method
# class A:
#     def m1(self):
#         print("this is M1 method from class A")
#
# class B(A):
#     def m1(self):
#         print("this is M2 method from class B")
#         super().m1()   # invoke the immediate parent class method
#
# bobj=B()
# bobj.m1()
#
# # example_7 calling parent class variable using child class
# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#
#     def m1(self,x,y):
#         print(x+y)
#         print(self.i+self.j)  # B class variable
#         print(self.a+self.b)  #A class variable
#
# bobj=B()
# bobj.m1(2,4)

# example_8 overriding variables

# class parent:
#     name="scott"
# class child(parent):
#     name="john"   #overrided variable
#     def m(self):
#         print(super().name)
#
# cobj = child()
# print(cobj.name)  # john   because it is overrided
# cobj.m()  # scott

# example_9:  overriding methods by using  Heirachry inheritance

class Tenth:
    def strengthOfPeople(self):
        return 0
class StudentsA(Tenth):
    def strengthOfPeople(self):
        return 26
class StudentsB(Tenth):
    def strengthOfPeople(self):
        return 30

students = StudentsA()
print(students.strengthOfPeople())

students= StudentsB()
print(students.strengthOfPeople())
