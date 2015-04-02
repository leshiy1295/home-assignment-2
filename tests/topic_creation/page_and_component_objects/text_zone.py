# -*- coding: utf-8 -*-

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests import Component, POLLING_TIME, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, MAXIMUM_WAIT_TIME_FOR_JS


__author__ = 'a.halaidzhy'


class TextZone(Component):
    def __init__(self, driver, is_short=False):
        super(TextZone, self).__init__(driver)
        if is_short:
            self.__TEXTAREA_ELEMENT = '//textarea[@id="id_text_short"]'
            self.__LABEL_FOR_ZONE = '//label[@for="id_text_short"]'
        else:
            self.__TEXTAREA_ELEMENT = '//textarea[@id="id_text"]'
            self.__LABEL_FOR_ZONE = '//label[@for="id_text"]'
        self.__NEAREST_ERROR_LABEL = '/preceding-sibling::*[contains(@class, "system-message-error")][last()]'
        self.__TEXT_ZONE_ERROR_LABEL = self.__LABEL_FOR_ZONE + self.__NEAREST_ERROR_LABEL
        self.__NEAREST_INPUT_ELEMENT_TO_GET = '/following::div[contains(@class, "CodeMirror-code")][1]/pre[1]'
        self.__TEXT_INPUT_ELEMENT_TO_GET = self.__TEXTAREA_ELEMENT + self.__NEAREST_INPUT_ELEMENT_TO_GET
        self.__NEAREST_INPUT_ELEMENT_TO_SET = '/following::div[@class="CodeMirror-scroll"]'
        self.__TEXT_INPUT_ELEMENT_TO_SET = self.__TEXTAREA_ELEMENT + self.__NEAREST_INPUT_ELEMENT_TO_SET
        self.__NEAREST_TOOLBAR = '/following::div[contains(@class, "editor-toolbar")][1]'
        self.__BOLD_ELEMENT = self.__TEXTAREA_ELEMENT + self.__NEAREST_TOOLBAR + \
            '/a[contains(@class, "markdown-editor-icon-bold")]'
        self.__ITALIC_ELEMENT = self.__TEXTAREA_ELEMENT + self.__NEAREST_TOOLBAR + \
            '/a[contains(@class, "markdown-editor-icon-italic")]'
        self.__QUOTE_ELEMENT = self.__TEXTAREA_ELEMENT + self.__NEAREST_TOOLBAR + \
            '/a[contains(@class, "markdown-editor-icon-quote")]'
        self.__UNORDERED_LIST_ELEMENT = self.__TEXTAREA_ELEMENT + self.__NEAREST_TOOLBAR + \
            '/a[contains(@class, "markdown-editor-icon-unordered-list")]'
        self.__ORDERER_LIST_ELEMENT = self.__TEXTAREA_ELEMENT + self.__NEAREST_TOOLBAR + \
            '/a[contains(@class, "markdown-editor-icon-ordered-list")]'
        self.__LINK_ELEMENT = self.__TEXTAREA_ELEMENT + self.__NEAREST_TOOLBAR + \
            '/a[contains(@class, "markdown-editor-icon-link")][1]'
        self.__IMAGE_INSERT_ELEMENT = self.__TEXTAREA_ELEMENT + self.__NEAREST_TOOLBAR + \
            '/a[contains(@class, "markdown-editor-icon-link")][1]'
        self.__IMAGE_LOAD_ELEMENT = self.__TEXTAREA_ELEMENT + self.__NEAREST_TOOLBAR + \
            '/a[contains(@class, "markdown-editor-icon-link")][2]'
        self.__USER_ADD_ELEMENT = self.__TEXTAREA_ELEMENT + self.__NEAREST_TOOLBAR + \
            '/a[contains(@class, "markdown-editor-icon-link")][2]'
        self.__PREVIEW_ELEMENT = self.__TEXTAREA_ELEMENT + self.__NEAREST_TOOLBAR + \
            '/a[contains(@class, "markdown-editor-icon-preview")]'
        self.__ADD_USER_POPUP = '//form[@id="form-users-search"]'
        self.__ADD_USER_INPUT = '//input[@id="search-user-login-popup"]'
        self.__SELECT_USER_TO_ADD = self.__ADD_USER_POPUP + '//p[contains(@class, "realname")]/a[1]'

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
            lambda d: d.find_element_by_xpath(self.__TEXT_INPUT_ELEMENT_TO_SET)
        )
        textarea = self.driver.find_element_by_xpath(self.__TEXT_INPUT_ELEMENT_TO_SET)
        actions = ActionChains(self.driver)
        actions.click(textarea)
        actions.send_keys(text)
        actions.perform()

    def get_text(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TEXT_INPUT_ELEMENT_TO_GET)
        )
        return self.driver.find_element_by_xpath(self.__TEXT_INPUT_ELEMENT_TO_GET).text

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
