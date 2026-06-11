import pytest

from playwright.sync_api import Page, expect

def test_checkbox(page: Page):
    global day
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)

    # 1) select single checkbox:-------------------------
    # Monday= page.get_by_label("Monday")
    # Monday.check()
    # expect(Monday).to_be_checked()
    page.wait_for_timeout(2000)

   #  2 selecting all the ckeckboxes:

    checkboxes =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # print("total no of checkboxes: ", len(checkboxes))

    days=[page.get_by_label(day) for day in checkboxes]
    print("total no of days: ", len(days))

    # for day in days:
    #     day.check()
    #     expect(day).to_be_checked()
    #     page.wait_for_timeout(2000)


#   unselect  last 3 checkboxes:
#     for day in days[-3:]:
#          day.uncheck()
#          expect(day).not_to_be_checked()
#          page.wait_for_timeout(2000)

# toggle checkboxes: it will check which is not checked and it will un chack which is checked
#     for day in days:
#         if day.is_checked():
#             day.uncheck()
#             expect(day).not_to_be_checked()
#             page.wait_for_timeout(2000)
#         else:
#             day.check()
#             expect(day).to_be_checked()
#             page.wait_for_timeout(2000)

    indexes=[1,3,6]
    for i in indexes:
        days[i].check()
        expect(days[i]).to_be_checked()
    page.wait_for_timeout(2000)











