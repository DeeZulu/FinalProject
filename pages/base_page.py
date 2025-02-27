import math

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """Проверка ссылки на логин"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка на логин отсутствует"

    def open(self):
        """Открытие браузера"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Есть ли элемент на странице
        :param how: css, id, xpath
        :param what: селектор
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=10):
        """Проверка что элемента нет"""
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
