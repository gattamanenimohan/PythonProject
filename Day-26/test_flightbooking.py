from execnet.script.socketserver import old
from playwright.sync_api import sync_playwright,expect,Page


# def test_flightbooking(page: Page):
#     travel_world = page.goto("https://blazedemo.com/")
#
#     page.wait_for_timeout(2000)
#     print("user able to open travel world booking page : ",travel_world)
#
# #   finding the text in the landing page:
#     heading= page.locator("h1")
#     expect(heading).to_have_text("Welcome to the Simple Travel Agency!")
#
#
# # selecting the dropdown:-------------------------
#     departure_city = page.locator("//select[@name='fromPort']").select_option(index=3)
#     print("departure  country is : ",departure_city)
#     page.wait_for_timeout(2000)
#
#     destination_city = page.locator("//select[@name='toPort']").select_option(index=2)
#     print("departure  country is : ", destination_city)
#     page.wait_for_timeout(2000)
#     page.locator("input[type='submit']").click()
#
#     page.wait_for_timeout(5000)


# changing the values in the form of tuple to list

mytuple = ("mohan", "apple", "banana", "krishna", "qualitest")
mylist = list(mytuple)
print("before modifying the values : ", mylist)
# mylist[2]="sweet"
# print("after modifying the values : ", mylist)
# mytuple=tuple(mylist)
# print(mytuple)
















