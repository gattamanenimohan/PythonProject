import page
import pytest

from playwright.sync_api import Playwright, Page, expect


def test_bootstrapdropdown(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#     login steps:

    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()


    # clickin gon PIM TAB:
    page.get_by_text("PIM").click()


#     Clicking on the job title dropdown:
    page.locator("form i").nth(2).click()
    page.wait_for_timeout(2000)

#     capture all the options in the list
    page.locator("div[role='listbox']")
    page.wait_for_timeout(2000)
    job_roles = page.locator("div[role='option']")

    # it is notting but to avoid spce in between the job roles and we can print the all available roles in list format
    total_no_roles= [text.strip() for text in job_roles.all_text_contents()]
    print("total no_roles is : ",total_no_roles)

    #  counting the no of the roles:
    count = job_roles.count()
    print("total no of job roles:", count)
    expect(job_roles).to_have_count(count)

    # selecting the job role:
    selected_role= job_roles.nth(3).inner_text()
    job_roles.nth(3).click()
    page.wait_for_timeout(2000)

    # printing the selected job role
    print("selected_role:",selected_role)
    page.wait_for_timeout(2000)

    # in looping statement printing all the roles in
    for i in total_no_roles:
        print("name of the role available : ",i)

    page.wait_for_timeout(2000)

    # for i in range(count):
    #    text=job_roles.nth(i).inner_text()
    #    if text=="Automaton Tester":
    #        job_roles.nth(i).click()
    #        break

