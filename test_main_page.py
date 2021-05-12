from .pages.main_page import MainPage
from .pages.login_page import LoginPage

#def go_to_login_page(browser)
#    login_link = browser.find_element_by_css_selector("#login_link")
#    login_link.click()

def test_guest_can_go_to_login_page(browser):    
#    browser.get(link)
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link) # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url-адрес
    page.open() # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
    #login_page = page.go_to_login_page() # запись в переменную метода перехода на новую страницу(1 метод перехода по страницам)
    login_page = LoginPage(browser, browser.current_url) # инициализируем LoginPage (2 метод перехода по страницам)
    login_page.should_be_login_page() # добавление метода другой страницы(страницы логина)

def test_gues_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link) 
    page.open()
    page.should_be_login_link()