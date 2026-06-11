# example for   method overloading  (polymorphism)

class calculation:
    def add(self,a=99,b=2,c=2):
        print(a+b+c)    # created only one method but we can use different forms

cal=calculation()   # but using different forms this is called overloading
cal.add()
cal.add(1,55,5)
cal.add(1,2,3)