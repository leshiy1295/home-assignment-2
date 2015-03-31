# -*- coding: utf-8 -*-

from tests import Page
from tests.auth_form import AuthForm

__author__ = 'a.halaidzhy'


class AuthPage(Page):

    @property
    def form(self):
        return AuthForm(self.driver)
