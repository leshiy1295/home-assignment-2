# -*- coding: utf-8 -*-

import os

from tests import SeleniumTest
from tests.authorization.page_and_component_objects.auth_page import AuthPage
from tests.topic_creation.page_and_component_objects.topic_creation_page import TopicCreationPage


__author__ = 'a.halaidzhy'


class TopicCreationTestCase(SeleniumTest):
    _PATH_TO_IMAGE = os.path.dirname(__file__) + '/res/image.jpg'

    def setUp(self):
        super(TopicCreationTestCase, self).setUp()
        AuthPage(self.driver).log_in()

    def test_start_state_of_page(self):
        topic_page = TopicCreationPage(self.driver)
        topic_page.open()

    def tearDown(self):
        super(TopicCreationTestCase, self).tearDown()
