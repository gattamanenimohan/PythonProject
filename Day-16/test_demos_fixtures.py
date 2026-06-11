# Fixture : re-usable function
#
# to use this fixtures repeatedly  need to add that function name in the place of parameter (this is parameter)
#  fixture is notting but before executing any test function.

# scope=function:- fixture will be called before every test function executes.
# scope="module":- fixture will be called only once before test function executes
# scope="class":- fixture will be called only once before the class
# scope="session":- fixtures will be called only once for session

import  pytest


@pytest.fixture
def setup():
    print("  setup browser...")

def test_one(setup):
    print("this is my test one ")

def test_two(setup):
    print("This is my test two")

def test_three(setup):
    print("this is my test three ")