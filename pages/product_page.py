from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def check_product_added_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        messages = self.browser.find_element(*ProductPageLocators.MESSAGES)
        assert f"{product_name.text} has been added to your basket" in messages.text,\
            f"Товар {product_name.text} не был добавлен в корзину"

    def compare_prices(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        assert product_price.text == basket_total.text, "Итоговая сумма в корзине отличается от стоимости товара\n" \
                                                        f"Корзина - {basket_total.text}\nТовар - {product_price.text}"
