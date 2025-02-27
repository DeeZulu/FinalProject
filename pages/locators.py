from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET = (By.XPATH, "//a[contains(text(), 'View basket')]")


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTRATION_FORM = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@value='Add to basket']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators:
    EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'Your basket is empty')]")
