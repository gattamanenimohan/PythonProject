import pytest

def test_LoginByEmail(setup):
    print("this is login by email test")   # to print we are using -S for result pass/fail -V using
    try:
        assert True==False
    except AssertionError:
        print("Assertion Error")

def test_LoginByFacebook(setup):
    print("this is login by facebook test")
    assert True==True

def test_LoginByMobile(setup):
    print("this is login by mobile test")
    assert True==True