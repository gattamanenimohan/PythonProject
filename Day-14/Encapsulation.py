# Example_1
#  to operat the variables only getter's and setter's method  we can operate

# to make it as private to follow "__marks" means # only through methods we can able to access the data
class Student:
    def __init__(self,name):
        self.name=name  #public variable
        self.__marks=30 # private variable

    def get_marks(self):
         return self.__marks

    def set_marks(self,marks):
        if marks<=100:
            self.__marks=marks
        else:
            print("marks should be less than 100")

stu=Student("mohan")
stu.set_marks(55)
stu.get_marks()
print(stu.get_marks())