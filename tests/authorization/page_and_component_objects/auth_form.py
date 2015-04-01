# -*- coding: utf-8 -*-

import os
from selenium.webdriver.support.wait import WebDriverWait
from tests import Component

__author__ = 'a.halaidzhy'


class AuthForm(Component):
    LOGIN = 'ftest16@tech-mail.ru'
    PASSWORD = os.environ.get('TTHA2PASSWORD', '')

    _FORM = '//form[@id="popup-login-form"]'

    _OPEN_FORM_ELEMENT = '//a[contains(@class, "trigger-login")]'
    _FORM_LOGIN_FIELD = _FORM + '//input[@name="login"]'
    _FORM_PASSWORD_FIELD = _FORM + '//input[@name="password"]'
    _FORM_ERROR_LABEL = _FORM + '//p[contains(@class, "validate-error-login")]'
    _FORM_SUBMIT_BUTTON = _FORM + '//button[@name="submit_login"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self._OPEN_FORM_ELEMENT).click()

    def set_login(self, login):
        self.driver.find_element_by_xpath(self._FORM_LOGIN_FIELD).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self._FORM_PASSWORD_FIELD).send_keys(password)

    def submit_form(self):
        self.driver.find_element_by_xpath(self._FORM_SUBMIT_BUTTON).click()

    def is_submit_button_disabled(self):
        return self.driver.find_element_by_xpath(self._FORM_SUBMIT_BUTTON).get_attribute('disabled')

    def log_in(self):
        self.open_form()
        self.set_login(self.LOGIN)
        self.set_password(self.PASSWORD)
        self.submit_form()

    def get_error_label_text(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self._FORM_ERROR_LABEL).text
        )
