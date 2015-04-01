# -*- coding: utf-8 -*-

from tests.redirects_to_topic_creation.page_and_component_objects.portal_main_page import PortalMainPage

__author__ = 'a.halaidzhy'


class TopicCreationPage(PortalMainPage):
    __PATH = 'blog/topic/create/'

    def open(self, path=__PATH):
        PortalMainPage(self.driver).top_menu.get_username()  # latency for correct authorization
        super(TopicCreationPage, self).open(path)
