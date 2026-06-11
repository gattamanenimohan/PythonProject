from openpyxl.styles.builtins import total
from playwright.sync_api import sync_playwright,expect,Page


def test_drop_down(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table= page.locator("table[name='BookTable']")
    expect(table).to_be_visible()

#1)  counting the no of the rows in the table
    rows= table.locator("tr") # actual xpath----- table[name='BookTable'] tr
    expect(rows).to_have_count(7)

    rows_count=rows.count()
    print("no of the rows present: ",rows_count)

# 2) counting the no of columns in the table
    columns = rows.locator("th")
#     columns = page.locator("table[name='BookTable'] tr th")
    expect(columns).to_have_count(4)

    columns_count=columns.count()
    print("no of columns present: ",columns_count)

# 3) read all the 2nd row data form the table:
    second_row_data = rows.nth(3).locator("td")
    second_row_text = second_row_data.all_inner_texts()
    print("second row text: ",second_row_text)
    # expect(second_row_data).to_have_text("['learn java', 'mukesh', 'java', '500']")

    print("printing 2nd row of the table")
    for text in second_row_text:
        print(text)

    print("printing all the  row's in the table")
    all_row_data = rows.all()

    # for rows in all_row_data[1:]:
    #     call_rows= rows.locator("td").all_inner_texts()
    #     print(call_rows)

    # printing book name which author is mukesh
    print("printing books name and author names")
    for rows in all_row_data[1:]:
        author_name= rows.locator("td").nth(1).inner_text()
        print("author_name: ", author_name)
        if author_name == "Mukesh":
            book_name= rows.locator("td").nth(0).inner_text()
            print("book_name: ", book_name)

    # printing the total price
    total_price=0

    for rows in all_row_data[1:]:
        price= rows.locator("td").nth(3).inner_text()
        total_price += int(price)
    print("total_price: ", total_price)


    page.wait_for_timeout(3000)