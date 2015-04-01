# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait

from tests import Component

__author__ = 'a.halaidzhy'


class TopMenu(Component):
    USERNAME = u'Лизонька Манилова'
    _USERNAME_ELEMENT = '//div[@id="dropdown-user"]//a[contains(@class, "username")]'
    _CREATE_BUTTON = '//a[@id="modal_write_show"]'
    _TOPIC_ELEMENT = '//div[@id="modal_write"]//li[contains(@class, "write-item-type-topic")]'
    _TOPIC_ELEMENT_IMAGE = _TOPIC_ELEMENT + '/a[1]'
    _TOPIC_ELEMENT_WORD = _TOPIC_ELEMENT + '/a[last()]'

    def get_username(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self._USERNAME_ELEMENT).text
        )

    def open_create_popup(self):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self._CREATE_BUTTON)
        )
        self.driver.find_element_by_xpath(self._CREATE_BUTTON).click()

    def choose_topic_by_word(self):
        WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self._TOPIC_ELEMENT_WORD)
        )
        self.driver.find_element_by_xpath(self._TOPIC_ELEMENT_WORD).click()

    def choose_topic_by_image(self):
        WebDriverWait(self.driver, 1, 0.1).until(
            lambda d: d.find_element_by_xpath(self._TOPIC_ELEMENT_IMAGE)
        )
        self.driver.find_element_by_xpath(self._TOPIC_ELEMENT_IMAGE).click()
