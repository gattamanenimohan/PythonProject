class student:
    def __init__(self,id,name,grade):
        self.id=id   #class variable
        self.name=name   #class variable
        self.grade =grade  #class variable

    def display(self):     #method-------
        print(self.id, self.name,self.grade)