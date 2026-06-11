from pydoc import text

import pytest

from playwright.sync_api import sync_playwright, expect, Page

# single select drop down
def test_drop_down(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # selected_country= page.locator("#country").select_option("India")  # by using label
    # selected_country= page.locator("#country").select_option(label="India")
    # # to check which country you have selected
    # print("selected country is :  ",selected_country)


    # selected_country=page.locator("#country").select_option(value="germany")
    # selected_country = page.locator("#country").select_option("germany")
    # print("user selected country is : ",selected_country)

    # by using index and    in this it will start's form  0
    selected_country = page.locator("#country").select_option(index=7)
    print("user selected country is : ",selected_country)
    page.wait_for_timeout(2000)

#     to find the total number of values and total text in one row
    total_options=page.locator("#country>option")
    option_text=[text.strip() for text in total_options.all_text_contents()]
    print("total options is : ",option_text)
    expect(total_options).to_have_count(10)

    for i in option_text:
        print("option text is : ",i)



