import pytest

from playwright.sync_api import Page,   expect


def test_radio(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)

    male_radio = page.locator("#male")

    # tto check either it should be visibility and enabled are not
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    # male radio button should not be chacked
    expect(male_radio).not_to_be_checked()
    page.wait_for_timeout(2000)

    # checked radion button:
    male_radio.check()
    page.wait_for_timeout(2000)

    # male radio button should be checked:
    expect(male_radio).to_be_checked()
    page.wait_for_timeout(2000)