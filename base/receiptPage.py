from base.locators import PagesLocators
from base.page import Page


class ReceiptPage(Page):
    def __init__(self, driver):
        self.locator = PagesLocators
        super(ReceiptPage, self).__init__(driver)

    def check_success_login(self):
        return self.find_element(*self.locator.SUCCESS_MESSAGE).text

    def check_page_loaded(self):
        return self.get_title()

    def is_init(self):
        return self.find_element(*self.locator.HEADER).is_displayed()
