from openpyxl.styles.builtins import total
from playwright.sync_api import sync_playwright,expect,Page
import re

def test_setup(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table= page.locator("table[id=taskTable] tbody")
    expect(table).to_be_visible()
    page.wait_for_timeout(200)
    return table.locator("tr").all()


def test_drop_down(page: Page):
    rows= test_setup(page)
    for row in rows:
        processer_name= row.locator("td").nth(0).inner_text()
        if processer_name == "System":
            cpu_load= row.locator("td:has-text('%')").inner_text()
            print("CPU load of Chrome process:",cpu_load)


def test_Memory(page: Page):
    rows= test_setup(page)
    for row in rows:
        processer_name = row.locator("td").nth(0).inner_text()
        if processer_name == "Firefox":
            firefox_process = row.locator("td").filter(has_text=re.compile(r"MB$")).nth(0).inner_text()
            print("Memory Size of Firefox process:",firefox_process)


def test_Network_speed(page: Page):
    rows= test_setup(page)
    for row in rows:
        processer_name = row.locator("td").nth(0).inner_text()
        if processer_name == "Chrome":
            network_speed = row.locator("td:has-text('Mbps')").inner_text()
            print("Network speed of Chrome process:",network_speed)


def test_Disk_space(page: Page):
    rows= test_setup(page)
    for row in rows:
        processer_name = row.locator("td").nth(0).inner_text()
        if processer_name == "Chrome":
            disk_space = row.locator("td:has-text('MB/s')").inner_text()
            page.wait_for_timeout(5000)
            print("Disk space of Firefox process:",disk_space)


    page.wait_for_timeout(5000)
    page.close()
