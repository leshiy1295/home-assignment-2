# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait

from tests import Component, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN


__author__ = 'a.halaidzhy'


class BlogDescription(Component):
    __SIDEBAR_BLOCK = '//aside[@id="sidebar"]'
    __HEADER_TITLE = __SIDEBAR_BLOCK + '//header[contains(@class, "block-header")]/h3'
    __DESCRIPTION_TITLE = '//p[@id="block_blog_info"]'

    def get_title(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__HEADER_TITLE)
        )
        return self.driver.find_element_by_xpath(self.__HEADER_TITLE).text

    def get_description(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__DESCRIPTION_TITLE)
        )
        return self.driver.find_element_by_xpath(self.__DESCRIPTION_TITLE).text
