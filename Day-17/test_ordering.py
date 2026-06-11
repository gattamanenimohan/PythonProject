# pre-request: install pytest-order plugin
# to install : pip install pytest-order

# if you are changing the positions also by using order format we can reorder it.

import pytest
# Approach-1 : order test by position like 1,  2,  3,

# @pytest.mark.order(3)
# def test_logout():
#     print("user able to logout successfully")
#
# @pytest.mark.order(2)
# def test_addtoCart():
#     print("user able to add cart successfully")
#
# @pytest.mark.order(1)
# def test_login():
#     print("user able to login successfully")

# Approach_2: using "before"    and    "after"

import pytest

# @pytest.mark.order()
# def test_logout():
#     print("logout successfully")
#
# @pytest.mark.order(1)
# def test_login():
#     print("Login successfully")
#
# @pytest.mark.order(before="test_logout")
# def test_addtoCart():
#     print("added items in the cart")


# Approach -3: using marker string (user defined)  first and last we can able use ----

@pytest.mark.order("last")
def test_logout():
    print("logout successfully")

@pytest.mark.order("first")
def test_login():
    print("Login successfully")

@pytest.mark.order()
def test_addtoCart():
    print("added items in the cart")




