import  pytest


@pytest.fixture
def setup():
    print("  setup browser...")
    return"chrome"   # fixtures returns the value's
    # yield
    # print("close browser")

def test_one(setup):
    print("this is my test one ")
    print("browser is :",setup)

def test_two(setup):
    print("This is my test two")

def test_three(setup):
    print("this is my test three ")