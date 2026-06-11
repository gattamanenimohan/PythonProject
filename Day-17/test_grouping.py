# grouping tests:
# --------------------
# def test_LoginByEmail--> sanity, regression
# def test_LoginByFacebook---> sanity
# def test_LoginByMobile---> regression
# test_signupbyEmial ---> sanity,regression
#  test_signupbyFacebook--->regression
#  test_signupbyPhone--->sanity
# test_paymentindollor----> sanity, regression
# test_paymentinrupees---> regression

import pytest

@pytest.mark.sanity
@pytest.mark.regression
def test_loginByEmail():
    print("user able to login email successfully")
    assert 1 == 1
@pytest.mark.sanity
def test_loginByFacebook():
    print("user able to login facebook successfully")
    assert 1 == 1

@pytest.mark.regression
def test_loginByPhone():
    print("user able to login phone successfully")
    assert 1 == 1
@pytest.mark.sanity
@pytest.mark.regression
def test_signupByEmail():
    print("user able to signup email successfully")
    assert 1 == 1
@pytest.mark.regression
def test_signupByFacebook():
    print("user able to signup facebook successfully")
    assert 1 == 1

@pytest.mark.sanity
def test_signupByPhone():
    print("user able to signup phone successfully")
    assert 1 == 1
@pytest.mark.sanity
@pytest.mark.regression
def test_paymentindollor():
    print("user able to pay indoler successfully")
    assert 1 == 1
@pytest.mark.regression
def test_paymentinrupee():
    print("user able to pay in rupees successfully")
    assert 1 == 1

# when you use user defined values at that time we can able to view warrings:
#  to avoid that we need to create one file that is in "pytest.ini" file.

# ex: requirement --

# 1)  only sanity
# pytest Day-17/test_grouping.py -s -v -m "sanity"           ---m is to identify during the grouping test statements

#2)n only regression
# pytest Day-17/test_grouping.py -s -v -m "regression"


# 3) both sanity & regression
# pytest Day-17/test_grouping.py -s -v -m "sanity and regression"

# 4)  only sanity which not belongs to regression-------
#pytest Day-17/test_grouping.py -s -v -m "sanity"-m " not regression"

# 5) only regression not  sanity-----------
#pytest Day-17/test_grouping.py -s -v -m "regression"-m " not sanity"