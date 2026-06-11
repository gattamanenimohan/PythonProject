from pydoc import text

import pytest

from playwright.sync_api import sync_playwright, expect, Page
from requests import options


# multiple select drop down
def test_multiselect_drop_down(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

#     selecting multiple options from the dropdown

    # selected_colors= page.locator("#colors").select_option(label=["Red","Green","Blue"]) # by using label
    # print(selected_colors)

    # using values
    # page.locator("#colors").select_option(value=["red","Green","white"]) # using values


    # by using index:
    # colors_selected=page.locator("#colors").select_option(index=[2,4,6])
    # print("selected colors are: ",colors_selected)
    # page.wait_for_timeout(2000)

    dropdown_options=page.locator("#colors>option")
    options_txt=[text.strip() for text in dropdown_options.all_text_contents()]
    print("selected options are: ",options_txt)
    expect(dropdown_options).to_have_count(7)

    for i in options_txt:
        print("total no of colors: ",i)




