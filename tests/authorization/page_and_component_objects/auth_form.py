# -*- coding: utf-8 -*-

import os

from selenium.webdriver.support.wait import WebDriverWait

from tests import Component, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME, MAXIMUM_WAIT_TIME_FOR_JS


__author__ = 'a.halaidzhy'


class AuthForm(Component):
    LOGIN = 'ftest16@tech-mail.ru'
    PASSWORD = os.environ.get('TTHA2PASSWORD', '')

    __FORM = '//form[@id="popup-login-form"]'

    __OPEN_FORM_ELEMENT = '//a[contains(@class, "trigger-login")]'
    __FORM_LOGIN_FIELD = __FORM + '//input[@name="login"]'
    __FORM_PASSWORD_FIELD = __FORM + '//input[@name="password"]'
    __FORM_ERROR_LABEL = __FORM + '//p[contains(@class, "validate-error-login")]'
    __FORM_SUBMIT_BUTTON = __FORM + '//button[@name="submit_login"]'

    def open_form(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__OPEN_FORM_ELEMENT)
        )
        self.driver.find_element_by_xpath(self.__OPEN_FORM_ELEMENT).click()

    def set_login(self, login):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__FORM_LOGIN_FIELD)
        )
        self.driver.find_element_by_xpath(self.__FORM_LOGIN_FIELD).send_keys(login)

    def set_password(self, password):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__FORM_PASSWORD_FIELD)
        )
        self.driver.find_element_by_xpath(self.__FORM_PASSWORD_FIELD).send_keys(password)

    def submit_form(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__FORM_SUBMIT_BUTTON)
        )
        self.driver.find_element_by_xpath(self.__FORM_SUBMIT_BUTTON).click()

    def is_submit_button_disabled(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__FORM_SUBMIT_BUTTON)
        )
        return self.driver.find_element_by_xpath(self.__FORM_SUBMIT_BUTTON).get_attribute('disabled')

    def log_in(self):
        self.open_form()
        self.set_login(self.LOGIN)
        self.set_password(self.PASSWORD)
        self.submit_form()

    def get_error_label_text(self):
        return WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__FORM_ERROR_LABEL).text
        )
