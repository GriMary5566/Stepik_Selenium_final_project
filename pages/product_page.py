from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD), "Button 'Add to basket' is not presented"

    def sheuld_alert_msg_add_product_to_bascet(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_MSG_ADD), "Alert with messadge about add product to basket is not presented"

    def sheuld_name_product_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_NAME), "Product's name is not presented in basket" 

    def sheuld_product_price_in_alert(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_PRODUCT_PRICE), "Product's price is not presented in alert"

    def add_product_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add.click()        
#        self.solve_quiz_and_get_code()
        time.sleep(3)
        msg_text = self.browser.find_element(*ProductPageLocators.ALERT_MSG_ADD).text
        produkt_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text 
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_product_price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE).text      
        assert  "has been added to your basket." in msg_text,\
            f"Wrong messadge. Instead '{produkt_name} has been added to your basket.' we get '{msg_text}'"
        assert alert_product_name == produkt_name,\
           f"Wrong product's name in basket. Instead '{produkt_name}' we get '{alert_product_name}'"
        assert alert_product_price == product_price,\
           f"Wrong product's price in basket. Instead '{product_price}' we get '{alert_product_price}'"

    def should_not_be_success_message_when_opening_product_page(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_MSG_ADD), \
           "Success message is presented when opening the product page, but should not be"

    def should_not_be_success_message_when_click_add_product_to_cart_button(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add.click()
        assert self.is_not_element_present(*ProductPageLocators.ALERT_MSG_ADD), \
           "Success message is presented when we click the add product to basket button, but should not be"     
    
    def should_disappeared_success_message(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add.click()
        assert self.is_disappeared(*ProductPageLocators.ALERT_MSG_ADD), \
           "Success message is presented, but should disappeared"
