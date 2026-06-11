from pydoc import text
from unittest.util import sorted_list_difference

import pytest

from playwright.sync_api import sync_playwright, expect, Page

# single select drop down
def test_drop_down(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # dropdown_options= page.locator("#colors>option")
    dropdown_options = page.locator("#animals>option")
    options_text= [text.strip() for text in dropdown_options.all_text_contents()]

    original_list=options_text.copy()
    print("before sorting: ",original_list)
    sorted_list= sorted(options_text)
    print("after sorting: ",sorted_list)

    if original_list==sorted_list:
        print("dropdown is sorted correctly")
    else:
        print("dropdown is not sorted correctly")



    page.wait_for_timeout(2000)







