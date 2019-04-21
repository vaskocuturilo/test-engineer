from base.page import Page
from base.locators import PagesLocators


class SignUpPage(Page):
    def __init__(self, driver):
        self.locator = PagesLocators
        super().__init__(driver)  # Python3 version

    def navigate_to(self):
        self.open("http://test-engineer.info/testroom/login.html")

    def enter_login(self, login):
        self.find_element(*self.locator.LOGIN).send_keys(login)

    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.SUBMIT).click()

    def enter_credentials(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.click_login_button()

