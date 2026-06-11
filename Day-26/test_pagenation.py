
from playwright.sync_api import sync_playwright,expect,Page
import pytest


def test_drop_down(page: Page):
    page.goto("https://datatables.net/")
    page.wait_for_timeout(2000)

    has_more_pages= True

    while has_more_pages:
        rows=page.locator('#example_wrapper tbody tr').all()
        for row in rows:
            print(row.inner_text())


        next_button=page.locator("button[aria-label='Next']")
        disable_button= next_button.get_attribute("class")
        page.wait_for_timeout(2000)

        if "disabled" in disable_button:
            has_more_pages= False
        else:
            next_button.click()

# for filtering the dropdown-----------------

def test_filter(page: Page):
    page.goto("https://datatables.net/")
    page.wait_for_timeout(2000)
    dropdown = page.locator("#dt-length-0")
    dropdown.select_option(label="25")
    page.wait_for_timeout(2000)

    rows=page.locator('#example_wrapper tbody tr')
    print("number of row's present: ",rows.count())
    expect(rows).to_have_count(25)











