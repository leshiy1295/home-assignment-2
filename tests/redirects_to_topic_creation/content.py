from selenium.webdriver.support.wait import WebDriverWait
from tests import Component

__author__ = 'a.halaidzhy'


class Content(Component):
    _TITLE_ELEMENT = '//div[@id="content"]//h2[contains(@class, "page-header")]'

    def get_title(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self._TITLE_ELEMENT).text
        )
