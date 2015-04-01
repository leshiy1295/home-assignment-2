# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait

from tests import Component, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME
from tests.topic_creation.page_and_component_objects.checkbox_zone import CheckBoxZone
from tests.topic_creation.page_and_component_objects.short_text_zone import ShortTextZone
from tests.topic_creation.page_and_component_objects.text_zone import TextZone


__author__ = 'a.halaidzhy'


class CreateTopicForm(Component):
    __FORM_ELEMENT = '//div[@id="content"]//form'
    __BLOG_NAME = '//div[@id="id_blog"]'
    __TOPIC_TITLE = '//input[@id="id_title"]'
    __SUBMIT_BUTTON = __FORM_ELEMENT + '//button[contains(@class, "button-primary")]'
    __NEAREST_ERROR_LABEL = '/preceding-sibling::*[contains(@class, "system-message-error")][last()]'

    def __get_error_label_path_for(self, element):
        if element == 'blog' or element == 'title':
            return '//label[contains(@for, "id_{}")]'.format(element) + self.__NEAREST_ERROR_LABEL

    def get_blog_name_error(self):
        return WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__get_error_label_path_for('blog')).text
        )

    def get_topic_header_error(self):
        return WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__get_error_label_path_for('title')).text
        )

    def get_blog_name(self):
        return WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__BLOG_NAME).text
        )

    def set_blog_name(self, text):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__BLOG_NAME)
        )
        select_element = self.driver.find_element_by_xpath(self.__BLOG_NAME)
        for option in select_element.find_elements_by_tag_name('option'):
            if option.text == text:
                option.click()
                break

    def get_topic_header(self):
        return WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TOPIC_TITLE).text
        )

    def set_topic_header(self, text):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TOPIC_TITLE)
        )
        self.driver.find_element_by_xpath(self.__TOPIC_TITLE).send_keys(text)

    @property
    def get_short_text_zone(self):
        return ShortTextZone(self.driver)

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
