from selenium.webdriver.support.wait import WebDriverWait
from tests import Page, POLLING_TIME, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN

__author__ = 'a.halaidzhy'


class TopicDeletionPage(Page):
    __DELETE_BUTTON = '//input[contains(@class, "button-primary")]'
    __CANCEL_BUTTON = '//button[contains(@class, "button-back")]'

    def press_delete_button(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__DELETE_BUTTON)
        )
        self.driver.find_element_by_xpath(self.__DELETE_BUTTON).click()

    def press_cancel_button(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__CANCEL_BUTTON)
        )
        self.driver.find_element_by_xpath(self.__CANCEL_BUTTON).click()
