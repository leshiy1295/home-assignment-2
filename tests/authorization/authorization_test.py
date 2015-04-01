# -*- coding: utf-8 -*-

import unittest
import os

from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from tests.authorization.page_and_component_objects.auth_form import AuthForm
from tests.authorization.page_and_component_objects.auth_page import AuthPage
from tests.redirects_to_topic_creation.portal_main_page import PortalMainPage


__author__ = 'a.halaidzhy'


class AuthorizationTestCase(unittest.TestCase):
    _WRONG_LOGIN = 'wrong_login'
    _WRONG_PASSWORD = ''
    _ERROR_MESSAGE = u"Что-то не так! Вероятно, неправильно указаны данные"

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def test_wrong_auth_data(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self._WRONG_LOGIN)
        auth_form.set_password(self._WRONG_PASSWORD)
        self.assertFalse(auth_form.is_submit_button_disabled())
        auth_form.submit_form()
        self.assertIn(self._ERROR_MESSAGE, auth_form.get_error_label_text())

    def test_right_auth_data(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(AuthForm.LOGIN)
        auth_form.set_password(AuthForm.PASSWORD)
        self.assertFalse(auth_form.is_submit_button_disabled())
        auth_form.submit_form()

        portal_main_page = PortalMainPage(self.driver)
        self.assertIn(portal_main_page.top_menu.USERNAME, portal_main_page.top_menu.get_username())

    def tearDown(self):
        self.driver.quit()
