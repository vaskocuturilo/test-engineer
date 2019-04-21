from selenium.webdriver.common.by import By


class PagesLocators(object):
    HEADER = (By.TAG_NAME, 'h1')
    LOGIN = (By.ID, 'login_field')
    PASSWORD = (By.ID, 'password_field')
    SUBMIT = (By.ID, 'login_button')
    ERROR_MESSAGE = (By.ID, 'message_error')
    SUCCESS_MESSAGE = (By.TAG_NAME, 'a')
