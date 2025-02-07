from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        """Проверка ссылки на логин"""
        assert self.is_element_present(By.XPATH, "//a[@id='login_link']"), "Ссылка на логин отсутствует"
