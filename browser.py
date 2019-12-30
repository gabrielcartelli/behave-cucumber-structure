from selenium import webdriver


class Browser(object):
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def browser_quit(self):
        self.driver.quit()
