import pytest
from playwright.sync_api import Page, expect

def test_xpath_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    # page.wait_for_timeout(2000)

# # 1) absolute xpath(full xpath)  --not recomended very less to use
#     logo=page.locator("//html[1]/body[1]/div[4]/div[1]/div[1]/div[1]/a[1]/img[1]")
#     expect(logo).to_be_visible()

# 2) relative xpath: //tagname[@attribute='value']
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible()

    page.wait_for_timeout(2000)

# 3) xpath with contains()------------------------
    products= page.locator("//h2//a[contains(@href,'computer')]")
    product_count = products.count()
    print("total products count:",(product_count))
    expect(products).to_have_count(product_count)

    # print("first computer product: ", products.first.inner_text())
    # print("last computer product: ", products.last.text_content())
    # print("nth computer product: ", products.nth(1).text_content()) # it will take index from 0

    # it will print all the product names in the form of list collections
#     product_title=products.all_text_contents()
#     print("product title:",product_title)
#
# #     it will print in the form of looping statements
#     for i in product_title:
#         print(i)

# xpath with product starts with-------------------
#     product_starts_with= page.locator("//h2//a[starts-with(@href,'/build')]")
#     print("total products count:", product_starts_with.count())
#     product_title= product_starts_with.all_text_contents()
#     print("product starts with:",product_title)
#     # expect(product_starts_with).to_have_count(product_starts_with.count())
#
#
#     print("total products count:", product_starts_with.count())
#     for i in product_title:
#         print(i)
# to

    # to find how many products and exart product title

    Build_product = page.locator("//h2//a[starts-with(@href,'/build')]")
    print("Build total product count:",Build_product.count())
    total_product_list=Build_product.all_text_contents()
    print("build total product title :",total_product_list)
    expect(Build_product).to_have_count(Build_product.count())

    for i in total_product_list:
        print(i)

#xpath with text() -is representing inner text of the element
    register_link= page.locator("//a[text()='Register']")
    expect(register_link).to_be_visible()
    print("register link :",register_link)
    page.wait_for_timeout(3000)

# xpath with position()-------------------
    youtubepluslink= page.locator("//div[@class='column follow-us']//li[position()=4]")  # for position to use
    expect(youtubepluslink).to_have_text("YouTube")
    print("YouTube :",youtubepluslink)
    page.wait_for_timeout(3000)


# xpath with last()-------------------
    googlepluslink = page.locator("//div[@class='column follow-us']//li[last()]")  # for position to use
    page.wait_for_timeout(3000)
    expect(googlepluslink).to_have_text("Google+")
    print("google link :",googlepluslink)





