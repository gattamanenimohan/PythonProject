import re


from pdfplumber import page
from playwright.sync_api import Page,expect

# page.get_by_role() to locate by explicit and implicit accessibility attributes.
# page.get_by_text() to locate by text content.
# page.get_by_label() to locate a form control by associated label's text.
# page.get_by_placeholder() to locate an input by placeholder.
# page.get_by_alt_text() to locate an element, usually image, by its text alternative.
# page.get_by_title() to locate an element by its title attribute.
# page.get_by_test_id() to locate an element based on its data-testid attribute (other attributes can be configured).


def test_verify_pwlocators(page: Page):
#     page.goto("https://demo.nopcommerce.com")
#     page.wait_for_timeout(5000)
#
# # 1) page.get_by_alt_text()
#     # when you are seeing the alt attribute by the time we need to use this
#     logo=page.get_by_alt_text("nopCommerce demo store")
#     expect(logo).to_be_visible()
#
# # 2) page.get_by_text()
#     page.get_by_text("Welcome to our store")
#     expect(page.get_by_text("Welcome to our store")).to_be_visible()  # ful test
#     expect(page.get_by_text("Welcome to")).to_be_visible()  # parallel  test
#     expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible() # reg expression
#
# # 3) page.get_by_role()
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.wait_for_timeout(5000)
    expect(page.get_by_role("heading", name="Register")).to_be_visible()
#
# # 4)# page.get_by_label()
#     page.get_by_label("First name:").fill("mohan")
#     page.wait_for_timeout(2000)
#     page.get_by_label("Last name:").fill("krishan")
#     page.wait_for_timeout(2000)
#     page.get_by_label("Email:").fill("mohan#123gmail.com")
#     page.wait_for_timeout(2000)
#
# # 5) page.get_by_placeholder()
#     page.get_by_placeholder("Search store").fill("apple macbook pro")
#     page.wait_for_timeout(2000)
#
# # 6) page.get_by_title()
#     page.wait_for_timeout(2000)
#
#     title= page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
#     expect(page.get_by_title("Home page link")).to_have_text("Home")
#     print("user successfully logged in the title page",title)
#
# # 7) page.get_by_test_id()
#     expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")



# ------------------------------------------------------
    # orange HRM need to create.
    # page.goto("https://opensource-demo.orangehrmlive.com/")
    # page.wait_for_timeout(5000)
    # page.get_by_placeholder("Username").fill("Admin")
    # page.wait_for_timeout(2000)
    # page.get_by_placeholder("Password").fill("admin123")
    # page.wait_for_timeout(100)
    # page.get_by_role("button", name="Login").click()
    # page.wait_for_timeout(5000)
    # heading=expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()
    # print("user able to find the hading", heading)
    # page.wait_for_timeout(1000)







    # pytest Day-19/test_pwlocatorsdemo.py -s -v --headed






















    # page.close()
