def converted_name(func, *args):
        printable_name = func.__name__.title().replace("_", " ")
        print(printable_name, *args)


def open_browser(browser_name):
        converted_name(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
        converted_name(go_to_companyname_homepage,page_url)

def find_registration_button_on_login_page(page_url, button_text):
        converted_name(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="https://google.com")
find_registration_button_on_login_page(page_url="https://google.com/", button_text="search")





