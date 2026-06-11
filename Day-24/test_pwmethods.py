from playwright.sync_api import sync_playwright, expect, Page


def test_comparisionofmethods(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    products= page.locator(".product-title")

    #1)------------------ inner_text() vs text_content()
    # print("inner text",products.nth(1).inner_text())   # returns actual text without any spaces
    # print("text content",products.nth(1).text_content())   # returns content with special character and spaces

    # count=products.count()

    # for i in range(count):
        # product_name= products.nth(i).text_content()
        # # by using strip it will remove unwanted data and print actual data as same as inner text output
        # print(product_name.strip())

        # product_name = products.nth(i).inner_text()
        # print(product_name)

    # 2)--------all_text_contents() vs all_inner_texts()

    # product_names= products.all_inner_texts()  # it is printing as a list format with out any special character and spaces
    product_names= products.all_text_contents()  # it is printing as a list format only but with spaces and hidden characters
    print("with all text contents: ",product_names)

    products_trimmed= [text.strip()for text in product_names]
    print("with all text contents: ",products_trimmed)

    count=products.count()
    print("total no of products : ",count)

    for i in products_trimmed:
        print("with all text contents: ",i)








    page.wait_for_timeout(2000)
