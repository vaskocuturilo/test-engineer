from base.basePage import BasePage
from base.receiptPage import ReceiptPage
from base.signUpPage import SignUpPage


class LoginPage(BasePage):

    def test_login(self):
        open_page = SignUpPage(self.driver)
        open_page.navigate_to()
        page_load = ReceiptPage(self.driver)
        self.assertTrue(page_load.is_init())
        self.assertEqual("The Test Room | Login page", page_load.get_title())
        page_enter_data = SignUpPage(self.driver)
        page_enter_data.enter_credentials("test", "test")
        page_verify = ReceiptPage(self.driver)
        self.assertEqual("Logout", page_verify.check_success_login())
