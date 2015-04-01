# -*- coding: utf-8 -*-

from tests import Page
from tests.authorization.page_and_component_objects.auth_form import AuthForm

__author__ = 'a.halaidzhy'


class AuthPage(Page):

    @property
    def form(self):
        return AuthForm(self.driver)

    def check_cookies(self):
        return list(self.driver.get_cookies())

    def log_in(self):
        self.open()
        self.form.log_in()
