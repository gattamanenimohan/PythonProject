#dynamic xpath means having single button but plays a multiple role:

# if having one button same for start and stop :
# xpath's--:
#
# //button[text()='START' or text()='STOP']
# //button[@name()='START' or @name()='STOP']
# //button[contains(@name,'st')]
# //button[starts-with(@name,'st')]
#
#
#
# css:
# ---
#
# button[name='start'],button[name='stop']
# button[name^='st']
import re

import pytest

from playwright.sync_api import Page, expect

# By using xpath:----------------------------------------------
# def test_dynamic_xpath(page: Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#     page.wait_for_timeout(2000)
#
#     for i in range(5):
#         button=page.locator("//button[text()='START' or text()='STOP']")
#         button.click()
#         page.wait_for_timeout(2000)
#  pytest Day-21/test_dynamicxpath.py -s -v --headed


# by using css-----------------------------------------

# def test_dynamic_css(page: Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#     page.wait_for_timeout(2000)
#
#     for i in range(11):
#         button=page.locator("button[name='start'],button[name='stop']")
#         button.click()
#         page.wait_for_timeout(2000)

# using playwright locator-----------------------------
def test_dynamic_css(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)

    for i in range(11):
        button=page.get_by_role("button",name=re.compile(r"ST.*"))
        button.click()
        page.wait_for_timeout(2000)

