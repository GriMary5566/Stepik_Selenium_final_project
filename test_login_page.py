from .pages.login_page import LoginPage


def test_guest_should_got_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link) 
    page.open()
    page.should_be_login_page()
    #page.should_be_login_url()

#def test_gues_should_see_login_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#    page = MainPage(browser, link) 
#    page.open()
#    page.should_be_login_form()

#def test_gues_should_see_register_form(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#    page = MainPage(browser, link) 
#    page.open()
#    page.should_be_register_form()