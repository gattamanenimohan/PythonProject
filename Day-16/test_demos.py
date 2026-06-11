import  pytest


# executing in functions  method -------------------------------------


def test_one():
    print("this is my test one ")

def test_two():
    print("This is my test two")

def test_three():
    print("this is my test three ")

#  (  -s  )to display  the print output to view in terminals page
# pytest Day-16/test_demos.py -s

# if you need to execute any few tests means
# pytest Day-16/test_demos.py::test_two -s

# displayed more information for each test statements./passed are failed
# pytest Day-16/test_demos.py -s -v ---------
# ------------------------------------------------------------------------


# executing in class methods:

class TestClass:
    def test_one(self):
        print("this is my TestClass one")

    def test_two(self):
        print("This is my TestClass two")

    def test_three(self):
        print("this is my TestClass three ")

