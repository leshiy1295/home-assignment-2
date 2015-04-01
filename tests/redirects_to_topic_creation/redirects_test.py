# -*- coding: utf-8 -*-

from tests import Page, SeleniumTest
from tests.authorization.page_and_component_objects.auth_page import AuthPage
from tests.redirects_to_topic_creation.page_and_component_objects.portal_main_page import PortalMainPage


__author__ = 'a.halaidzhy'


class RedirectsTestCase(SeleniumTest):
    __TOPIC_CREATE_URL = Page.BASE_URL + 'blog/topic/create/'
    __TOPIC_CREATE_PAGE_HEADER = u'Создание топика'

    def setUp(self):
        super(RedirectsTestCase, self).setUp()
        AuthPage(self.driver).log_in()

    def test_open_topic_creation_by_word(self):
        portal_main_page = PortalMainPage(self.driver)
        top_menu = portal_main_page.top_menu

        top_menu.open_create_popup()
        top_menu.choose_topic_by_word()

        content = portal_main_page.content
        self.assertIn(self.__TOPIC_CREATE_PAGE_HEADER, content.get_title())
        self.assertEqual(self.driver.current_url, self.__TOPIC_CREATE_URL)

    def test_open_topic_creation_by_image(self):
        portal_main_page = PortalMainPage(self.driver)
        top_menu = portal_main_page.top_menu

        top_menu.open_create_popup()
        top_menu.choose_topic_by_image()

        content = portal_main_page.content
        self.assertIn(self.__TOPIC_CREATE_PAGE_HEADER, content.get_title())
        self.assertEqual(self.driver.current_url, self.__TOPIC_CREATE_URL)

    def tearDown(self):
        super(RedirectsTestCase, self).tearDown()
