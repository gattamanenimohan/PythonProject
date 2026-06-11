class employee:
    def __init__(self,eid,esal,ename):
        self.eid=eid   #class variable
        self.esal=esal   #class variable
        self.ename = ename  #class variable

    def display(self):     #method-------
        # print("empid:{} empsal:{}, empname:{}".format(self.eid,self.esal,self.ename))
        print(self.eid, self.esal, self.ename)