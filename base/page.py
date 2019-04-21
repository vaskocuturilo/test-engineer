class Page(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url
