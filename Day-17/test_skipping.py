import pytest


# select all + ctrl+alt+l   to make entire code in a correct format.

#  to run the program in terminal  is ----  pytest Day-17/test_skipping.py -s -v
#  for skipping the perticulat test cases we need to use this annotation/////////-----@pytest.mark.skip----////////

@pytest.fixture
def setup():
    print("user launched the browser successfully")
    yield
    print("user closed the browser successfully")

def test_loginByEmail(setup):
    print("user able to login email successfully")
    assert 1 == 1

def test_loginByFacebook(setup):
    print("user able to login facebook successfully")
    assert 1 == 1

@pytest.mark.skip
def test_loginByPhone(setup):
    print("user able to login phone successfully")
    assert 1 == 1
@pytest.mark.skip
def test_signupByEmail(setup):
    print("user able to signup email successfully")
    assert 1 == 1

def test_signupByFacebook(setup):
    print("user able to signup facebook successfully")
    assert 1 == 1

@pytest.mark.skip
def test_signupByPhone(setup):
    print("user able to signup phone successfully")
    assert 1 == 1
