import pytest

from playwright.sync_api import Page, expect

# tag ID,               tag#id
# tag class,            tag.class
# tag attribute,        tag[attribute=value]
# tag class attribute,  tag.class[attribute=value]



def test_inputbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)

    first_name = page.locator("input#name")
    # filling the text:
    first_name.fill("mohan")
    page.wait_for_timeout(2000)

    # ge the input value form input box:

    entered_value = first_name.input_value()
    print("entered value: ", entered_value)

    # to check either it should be visibility and enabled are not
    expect(first_name).to_be_visible()

    expect(first_name).to_be_enabled()

    # to get the attribute of the element
    page.wait_for_timeout(2000)
    first_name= first_name.get_attribute("placeholder")
    print("first_name get_attribute: ",first_name )

    # filling the text:
    # first_name.fill("mohan")


