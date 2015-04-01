import unittest
import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from tests import Page
from tests.authorization.page_and_component_objects.auth_page import AuthPage
from tests.redirects_to_topic_creation.portal_main_page import PortalMainPage


__author__ = 'a.halaidzhy'


class RedirectsTestCase(unittest.TestCase):
    _TOPIC_CREATE_URL = Page.BASE_URL + 'blog/topic/create/'

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        AuthPage(self.driver).log_in()

    def test_open_topic_creation_by_word(self):
        portal_mail_page = PortalMainPage(self.driver)
        top_menu = portal_mail_page.top_menu

        top_menu.open_create_popup()
        top_menu.choose_topic_by_word()

        self.assertEqual(self.driver.current_url, self._TOPIC_CREATE_URL)

    def test_open_topic_creation_by_image(self):
        portal_mail_page = PortalMainPage(self.driver)
        top_menu = portal_mail_page.top_menu

        top_menu.open_create_popup()
        top_menu.choose_topic_by_image()

        self.assertEqual(self.driver.current_url, self._TOPIC_CREATE_URL)

    def tearDown(self):
        self.driver.quit()
