from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller


class BasePage:

    def __init__(self):
        chromedriver_autoinstaller.install()
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.browser, timeout=5)
        self.action = webdriver.ActionChains(self.browser)

    def get_text(self, locator):
        el = self.wait_visible(locator)
        return el.text

    def get_empty_text(self, locator):
        el = self._wait_presence(locator)
        return el.text

    def move_to_element(self, locator):
        el = self.wait_visible(locator)
        self.action.move_to_element(el).perform()
        return el

    def move_to_element_with_offset(self, locator):
        el = self.browser.find_element(*locator)
        self.action.move_to_element_with_offset(el, 100, 0).click().perform()

    def switch_to_active_element(self):
        active_el = self.browser.switch_to.active_element
        return active_el

    def move_to_element_and_click(self, locator):
        el = self.wait_visible(locator)
        self.action.move_to_element(el).perform()
        el.click()

    def double_click(self):
        self.action.double_click().perform()

    def find_link(self, url):
        element = self.browser.find_element_by_xpath('//a[@href="' + url + '"]')
        return element

    def wait_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def _wait_presence(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))