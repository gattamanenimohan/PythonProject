
# pytest Day-18-PW/test_Playwright.py -s -v --headed  ---to test in terminal page

from playwright.sync_api import Page, expect

def test_verifypageURL(page: Page):  # 'page' is a built-in fixture
    # Navigate to Amazon
    page.goto("https://www.amazon.com")

    # Validate the expected URL
    expect(page).to_have_url("https://www.amazon.com/")

    # printing the statement
    myurl = page.url
    print("URL of the application", myurl)

def test_verifypageTitle(page: Page):
    # Navigate to Amazon
    page.goto("https://www.amazon.com")

    # validate the expected title
    # expect(page).to_have_title("Amazon.com. Spend less. Smile more.")
    expect(page).to_have_title("Amazon.com")

    # Printing the statement
    mytitle = page.title
    print("Title of the application", mytitle)

# for parallel testing:
# pytest Day-18-PW/test_Playwright.py -s -v --headed  -n 2   it will execute different browser at a time.