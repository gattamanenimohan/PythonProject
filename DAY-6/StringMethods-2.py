# isdecimal()
# isdigit()
# isNumberic()

from selenium.webdriver.common.devtools.v142 import page

# is decimal

print("123".isdecimal())
print("11.4".isdecimal())

a=12.3
b=123
c= "mohan"
print(type(a))
print(type(b))
print(type(c))


#isdigit()
# return true is all the character are digits.
# digits include decimal digits (0-9)
# allow other digit characters, such as superscripts,subscripts digits or digits from other numerical system.
# does not consider superscripts, fractions,or roman numerical as valid decimals

# from playwright.sync_api import sync_playwright
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context()
#
#     # Open first page (original window)
#     page1 = context.new_page()
#     page1.goto("https://www.example.com")
#     print("Original window:", page1.title())
#
#     # Open new window (Google)
#     page2 = context.new_page()
#     page2.goto("https://www.google.com")
#     print("Now in Google window:", page2.title())
#
#     # Open new window (Amazon)
#     page3 = context.new_page()
#     page3.goto("https://www.amazon.com")
#     print("Now in Amazon window:", page3.title())
#
#     # Switch back to original window
#     page1.bring_to_front()
#     print("Back to original window:", page1.title())
#
#     browser.close()

# split(): splitting strings
# list of deli metres- space,@,#,& ,;, :
s="mohan@gmail.com#12345"
lst=s.split("@")
print(lst)
print(lst[0])
print(lst[1])

#
a="one two three"
list=a.split(" ")
print("separating the data in to the list :", list)


# startswith()
s="welcome"
print(s.startswith("wel"))
print(s.startswith("Wel"))  # it is case censitive


# endswith()
s="welcome"
print(s.endswith("me"))
print(s.endswith("Me"))  # it is case censitive

# Trimming spaces Strip(), lstrip(), rstrip()
s="    welcome    "
print(s.strip())
print(s.lstrip())
print(s.rstrip())




hello= "my first name is : mohan and my second nams is : krishna"

list = hello.split(" ")
print(list)