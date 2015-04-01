# -*- coding: utf-8 -*-

from tests import SeleniumTest

from tests.authorization.page_and_component_objects.auth_form import AuthForm
from tests.authorization.page_and_component_objects.auth_page import AuthPage
from tests.redirects_to_topic_creation.page_and_component_objects.portal_main_page import PortalMainPage


__author__ = 'a.halaidzhy'


class AuthorizationTestCase(SeleniumTest):
    __WRONG_LOGIN = 'wrong_login'
    __WRONG_PASSWORD = ''
    __ERROR_MESSAGE = u"Что-то не так! Вероятно, неправильно указаны данные"

    def setUp(self):
        super(AuthorizationTestCase, self).setUp()

    def test_wrong_auth_data(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(self.__WRONG_LOGIN)
        auth_form.set_password(self.__WRONG_PASSWORD)
        self.assertFalse(auth_form.is_submit_button_disabled())
        auth_form.submit_form()
        self.assertIn(self.__ERROR_MESSAGE, auth_form.get_error_label_text())

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
        super(AuthorizationTestCase, self).tearDown()
