import  pytest


@pytest.fixture
def setup():
    print("  setup browser...")  # it will execute before the every test function
    yield
    print("close browser")   # it will execute after completion of every test function

def test_one(setup):
    print("this is my test one ")


def test_two(setup):
    print("This is my test two")

def test_three(setup):
    print("this is my test three ")