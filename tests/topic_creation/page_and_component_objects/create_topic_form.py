# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait

from tests import Component, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME
from tests.topic_creation.page_and_component_objects.checkbox_zone import CheckBoxZone
from tests.topic_creation.page_and_component_objects.text_zone import TextZone


__author__ = 'a.halaidzhy'


class CreateTopicForm(Component):
    BLOG_NAME = u'Флудилка'
    __FORM_ELEMENT = '//div[@id="content"]//form'
    __BLOG_NAME_SELECT = '//a[contains(@class, "chzn-single")]'
    __BLOG_NAME_OPTION = u'//li[contains(text(), "{}")]'.format(BLOG_NAME)
    __BLOG_NAME = '//div[@id="id_blog_chzn"]//span[1]'
    __TOPIC_TITLE = '//input[@id="id_title"]'
    __SUBMIT_BUTTON = __FORM_ELEMENT + '//button[contains(@class, "button-primary")]'
    __NEAREST_ERROR_LABEL = '/preceding-sibling::*[contains(@class, "system-message-error")][last()]'

    def __get_error_label_path_for(self, element):
        if element == 'blog' or element == 'title':
            return '//label[contains(@for, "id_{}")]'.format(element) + self.__NEAREST_ERROR_LABEL

    def get_blog_name_error(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__get_error_label_path_for('blog'))
        )
        return self.driver.find_element_by_xpath(self.__get_error_label_path_for('blog')).text

    def get_topic_header_error(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__get_error_label_path_for('title'))
        )
        return self.driver.find_element_by_xpath(self.__get_error_label_path_for('title')).text

    def get_blog_name(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__BLOG_NAME)
        )
        return self.driver.find_element_by_xpath(self.__BLOG_NAME).text

    def click_on_select_blog_name(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__BLOG_NAME_SELECT)
        )
        self.driver.find_element_by_xpath(self.__BLOG_NAME_SELECT).click()

    def set_blog_name(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__BLOG_NAME_OPTION)
        )
        self.driver.find_element_by_xpath(self.__BLOG_NAME_OPTION).click()

    def get_topic_header(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TOPIC_TITLE)
        )
        return self.driver.find_element_by_xpath(self.__TOPIC_TITLE).text

    def set_topic_header(self, text):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TOPIC_TITLE)
        )
        self.driver.find_element_by_xpath(self.__TOPIC_TITLE).send_keys(text)

    @property
    def get_short_text_zone(self):
        return TextZone(self.driver, True)

    @property
    def get_text_zone(self):
        return TextZone(self.driver)

    @property
    def get_checkbox_zone(self):
        return CheckBoxZone(self.driver)

    def submit_form(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__SUBMIT_BUTTON)
        )
        self.driver.find_element_by_xpath(self.__SUBMIT_BUTTON).click()
