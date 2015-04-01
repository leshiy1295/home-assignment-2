# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait

from tests import Component, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME

__author__ = 'a.halaidzhy'


class TopMenu(Component):
    USERNAME = u'Лизонька Манилова'
    __USERNAME_ELEMENT = '//div[@id="dropdown-user"]//a[contains(@class, "username")]'
    __CREATE_BUTTON = '//a[@id="modal_write_show"]'
    __TOPIC_ELEMENT = '//div[@id="modal_write"]//li[contains(@class, "write-item-type-topic")]'
    __TOPIC_ELEMENT_IMAGE = __TOPIC_ELEMENT + '/a[1]'
    __TOPIC_ELEMENT_WORD = __TOPIC_ELEMENT + '/a[last()]'

    def get_username(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__USERNAME_ELEMENT)
        )
        return self.driver.find_element_by_xpath(self.__USERNAME_ELEMENT).text

    def open_create_popup(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__CREATE_BUTTON)
        )
        self.driver.find_element_by_xpath(self.__CREATE_BUTTON).click()

    def choose_topic_by_word(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TOPIC_ELEMENT_WORD)
        )
        self.driver.find_element_by_xpath(self.__TOPIC_ELEMENT_WORD).click()

    def choose_topic_by_image(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TOPIC_ELEMENT_IMAGE)
        )
        self.driver.find_element_by_xpath(self.__TOPIC_ELEMENT_IMAGE).click()
