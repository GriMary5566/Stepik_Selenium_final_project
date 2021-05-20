from .base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):
    def should_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
           "There are products in the basket, but there should not be"


    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_AMPTY),\
            "The text 'Your basket is empty' is not present"
