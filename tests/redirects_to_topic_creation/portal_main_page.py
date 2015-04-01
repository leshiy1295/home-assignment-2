# -*- coding: utf-8 -*-

from tests import Page
from tests.redirects_to_topic_creation.top_menu import TopMenu

__author__ = 'a.halaidzhy'


class PortalMainPage(Page):

    @property
    def top_menu(self):
        return TopMenu(self.driver)
