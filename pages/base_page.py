from browser import Browser


class BasePage(Browser):
    def access_page(self, url):
        self.driver.get(url)

    def get_element(self, *locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((locator[0], locator[1])))
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.get_element(*locator).click()

    def get_text(self, *locator):
        return self.get_element(*locator).text
