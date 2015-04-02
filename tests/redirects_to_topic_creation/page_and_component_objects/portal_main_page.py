# -*- coding: utf-8 -*-

from tests import Page
from tests.redirects_to_topic_creation.page_and_component_objects.content import Content
from tests.redirects_to_topic_creation.page_and_component_objects.top_menu import TopMenu

__author__ = 'a.halaidzhy'


class PortalMainPage(Page):

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def content(self):
        return Content(self.driver)

    def is_topic_removed(self, topic_info):
        return not self.content.topic_exists(topic_info)

