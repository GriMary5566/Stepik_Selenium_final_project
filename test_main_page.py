from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
import pytest




def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link) 
    page.open() 
    page.go_to_login_page() 
    #login_page = page.go_to_login_page() # запись в переменную метода перехода на новую страницу(1 метод перехода по страницам)
    login_page = LoginPage(browser, browser.current_url) # инициализируем LoginPage (2 метод перехода по страницам)
    login_page.should_be_login_page() # добавление метода другой страницы(страницы логина)

def test_gues_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link) 
    page.open()
    page.should_be_login_link()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) 
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)    
    basket_page.should_no_products_in_basket()
    basket_page.should_be_text_basket_is_empty()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link) 
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)        
    basket_page.should_no_products_in_basket()
    basket_page.should_be_text_basket_is_empty()
