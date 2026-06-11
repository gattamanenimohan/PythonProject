import re
from itertools import count

import pytest
# relative CSS selector.

# tag ID,               tag#id
# tag class,            tag.class
# tag attribute,        tag[attribute=value]
# tag class attribute,  tag.class[attribute=value]

# Absolute CSS selector means :
# combination of multiple tags like : html>body>div>div>div>div[class='header-logo']

from playwright.sync_api import Page,expect

# def test_verify_css_locators(page:Page):
#     page.goto("https://demowebshop.tricentis.com/")
#     page.screenshot(path="chromium_maximized.png")
#     page.wait_for_timeout(2000)

    # tag-ID
    # page.locator("input#small-searchterms").fill("t-shirt")
    # page.locator("#small-searchterms").fill("t-shirt") # tag is optional.

    # tag.calss---
    # page.locator(".search-box-text").fill("t-shirt")
    # # page.locator("input.search-box-text").fill("t-shirt")

    # tag[attribute = value]

    # page.locator("input[name=q]").fill("t-shirt")
    # search=page.locator("[name=q]").fill("t-shirt")
    # page.wait_for_timeout(2000)
    # print("user able to type in search field",search)

    # tag.class[attribute=value]
    # page.locator("input.search-box-text[value='Search store']").fill("t-shirt")
    # page.locator(".search-box-text[value='Search store']").fill("t-shirt") # tag is optional
    # page.wait_for_timeout(2000)

    # page.get_by_alt_text("html>body>div>div>div>div[class='header-logo']").to_be_visible()
#
# if you having multiple tags but you need to fing only 1 at time:

# body>div>*.first-child
# body>div>*.nth-child(3)  1, 2, 3, 4, if depends on
# body>div>*.last-child

# if the text is starting with:
# p[class^='ma']------cap symbol

# if the text is end's with :
# p[class$='ub']------dollar symbol

# if the text is represent any where:
# p[class*='ub']------star symbol

# ------Assignment -1--------------------------------------------------------------------------------
#
def test_verify_css_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.screenshot(path="chromium_maximized.png")
    page.wait_for_timeout(2000)

    # 2
    # Create locator for logo
    logo=expect(page.locator("img[alt='Tricentis Demo Web Shop']")).to_be_visible()
    print(logo)

    #testecase_3 count no of the computers are present:

    computer=page.locator("div.product-item").filter(has_text="Computer")
    print("user able to find the computer : ",computer)
    count=computer.count()
    assert count == 4, f"Expected 4 computer products, but found {count}"
    page.wait_for_timeout(2000)

#   test_case:4 name of the nth product and price
    first_product_name=page.locator("div.product-item").nth(4).locator("h2 a")
    first_product_price= page.locator("div.product-item").nth(4).locator("div.add-info div.prices span")
    page.wait_for_timeout(2000)
    product= first_product_name.inner_text()
    price = first_product_price.inner_text()

    print("nth product name:",product)
    print("nth product price:",price)

#test_case:5 name of the first product and price
    first_product_name=page.locator("div.product-item").first.locator("h2 a")
    first_product_price= page.locator("div.product-item").first.locator("div.add-info div.prices span")
    page.wait_for_timeout(2000)
    product= first_product_name.inner_text()
    price = first_product_price.inner_text()
    print("my first product name:",product)
    print("my first product price:",price)


#test_case:5 name of the last product and price
    last_product_name=page.locator("div.product-item").last.locator("h2 a")
    last_product_price= page.locator("div.product-item").last.locator("div.add-info div.prices span")
    page.wait_for_timeout(2000)
    product= last_product_name.inner_text()
    price = last_product_price.inner_text()
    print("my last product name:",product)
    print("my last product price:",price)





    # test case:8 footer section names :
    first_name  = page.locator("div.footer li.facebook").first.locator("a")
    name =first_name.inner_text()
    print("my first name:",name)

    last_name = page.locator("div.footer li.google-plus").last.locator("a")
    name = last_name.inner_text()
    print("my last name :", name)
    #
    nth = page.locator("div.footer a").nth(3)
    name = nth.inner_text()
    print("my nth  name:", name)



    # printing all the computers names


 # Define locators
 #

