# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests import Component, POLLING_TIME, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, MAXIMUM_WAIT_TIME_FOR_JS


__author__ = 'a.halaidzhy'


class TextZone(Component):
    __NEAREST_ERROR_LABEL = '/preceding-sibling::*[contains(@class, "system-message-error")][last()]'
    __LABEL_FOR_ZONE = '//label[@for="id_text_short"]'
    __TEXT_ZONE_ERROR_LABEL = __LABEL_FOR_ZONE + __NEAREST_ERROR_LABEL
    __TEXTAREA_ELEMENT = '//textarea[@id="id_text_short"]'
    __NEAREST_INPUT_ELEMENT = '/following::div[contains(@class, "CodeMirror-code")][1]/pre[1]'
    __TEXT_INPUT_ELEMENT = __TEXTAREA_ELEMENT + __NEAREST_INPUT_ELEMENT
    __NEAREST_TOOLBAR = '/following::div[contains(@class, "editor-toolbar")][1]'
    __BOLD_ELEMENT = __TEXTAREA_ELEMENT + __NEAREST_TOOLBAR + '/a[contains(@class, "markdown-editor-icon-bold")]'
    __ITALIC_ELEMENT = __TEXTAREA_ELEMENT + __NEAREST_TOOLBAR + '/a[contains(@class, "markdown-editor-icon-italic")]'
    __QUOTE_ELEMENT = __TEXTAREA_ELEMENT + __NEAREST_TOOLBAR + '/a[contains(@class, "markdown-editor-icon-quote")]'
    __UNORDERED_LIST_ELEMENT = __TEXTAREA_ELEMENT + __NEAREST_TOOLBAR + \
        '/a[contains(@class, "markdown-editor-icon-unordered-list")]'
    __ORDERER_LIST_ELEMENT = __TEXTAREA_ELEMENT + __NEAREST_TOOLBAR + \
        '/a[contains(@class, "markdown-editor-icon-ordered-list")]'
    __LINK_ELEMENT = __TEXTAREA_ELEMENT + __NEAREST_TOOLBAR + '/a[contains(@class, "markdown-editor-icon-link")][1]'
    __IMAGE_INSERT_ELEMENT = __TEXTAREA_ELEMENT + __NEAREST_TOOLBAR + \
        '/a[contains(@class, "markdown-editor-icon-link")][1]'
    __IMAGE_LOAD_ELEMENT = __TEXTAREA_ELEMENT + __NEAREST_TOOLBAR + \
        '/a[contains(@class, "markdown-editor-icon-link")][2]'
    __USER_ADD_ELEMENT = __TEXTAREA_ELEMENT + __NEAREST_TOOLBAR + '/a[contains(@class, "markdown-editor-icon-link")][2]'
    __PREVIEW_ELEMENT = __TEXTAREA_ELEMENT + __NEAREST_TOOLBAR + '/a[contains(@class, "markdown-editor-icon-preview")]'
    __ADD_USER_POPUP = '//form[@id="form-users-search"]'
    __ADD_USER_INPUT = '//input[@id="search-user-login-popup"]'
    __SELECT_USER_TO_ADD = __ADD_USER_POPUP + '//p[contains(@class, "realname")]/a[1]'

    def __set_tool(self, path):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(path)
        )
        self.driver.find_element_by_xpath(path).click()

    def get_error_label(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TEXT_ZONE_ERROR_LABEL)
        )
        return self.driver.find_element_by_xpath(self.__TEXT_ZONE_ERROR_LABEL).text

    def set_text(self, text):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TEXT_INPUT_ELEMENT)
        )
        self.driver.find_element_by_xpath(self.__TEXT_INPUT_ELEMENT).send_keys(text)

    def get_text(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TEXT_INPUT_ELEMENT)
        )
        return self.driver.find_element_by_xpath(self.__TEXT_INPUT_ELEMENT).text

    def set_bold_tool(self):
        return self.__set_tool(self.__BOLD_ELEMENT)

    def set_italic_tool(self):
        return self.__set_tool(self.__ITALIC_ELEMENT)

    def set_quote_tool(self):
        return self.__set_tool(self.__QUOTE_ELEMENT)

    def set_unordered_list_tool(self):
        return self.__set_tool(self.__UNORDERED_LIST_ELEMENT)

    def set_ordered_list_tool(self):
        return self.__set_tool(self.__ORDERER_LIST_ELEMENT)

    def set_link_tool(self):
        return self.__set_tool(self.__LINK_ELEMENT)

    def set_image_insert_tool(self):
        return self.__set_tool(self.__IMAGE_INSERT_ELEMENT)

    def set_image_load_tool(self):
        return self.__set_tool(self.__IMAGE_LOAD_ELEMENT)

    def set_user_add_tool(self):
        return self.__set_tool(self.__USER_ADD_ELEMENT)

    def set_preview_tool(self):
        return self.__set_tool(self.__PREVIEW_ELEMENT)

    def set_user_to_add(self, user):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__ADD_USER_INPUT)
        )
        self.driver.find_element_by_xpath(self.__ADD_USER_INPUT).send_keys(user)

    def select_user(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__SELECT_USER_TO_ADD)
        )
        self.driver.find_element_by_xpath(self.__SELECT_USER_TO_ADD).click()

    def open_alert_to_set_link(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            EC.alert_is_present()
        )

    def dismiss_alert(self):
        alert = self.driver.switch_to_alert()
        alert.dismiss()

    def set_link_in_alert(self, link):
        alert = self.driver.switch_to_alert()
        alert.send_keys(link)
        alert.accept()

    def upload_image(self, path):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__IMAGE_LOAD_ELEMENT)
        )
        image_loader = self.driver.find_element_by_xpath(self.__IMAGE_LOAD_ELEMENT)
        image_loader.click()
        image_loader.clear()
        image_loader.send_keys(path)
