# -*- coding: utf-8 -*-

import os

from tests import SeleniumTest
from tests.authorization.page_and_component_objects.auth_page import AuthPage
from tests.topic_creation.page_and_component_objects.topic_creation_page import TopicCreationPage


__author__ = 'a.halaidzhy'


class TopicCreationTestCase(SeleniumTest):
    __PATH_TO_IMAGE = os.path.dirname(__file__) + '/res/image.jpg'
    __START_CREATE_TOPIC_PAGE_TITLE = u'Создание топика'
    __START_BLOG_DESCRIPTION_TITLE = u'Описание блога'
    __START_BLOG_DESCRIPTION = u'Выберите блог'
    __START_BLOG_NAME = u'-' * 9

    def setUp(self):
        super(TopicCreationTestCase, self).setUp()
        AuthPage(self.driver).log_in()

    def test_start_state_of_page(self):
        topic_page = TopicCreationPage(self.driver)
        topic_page.open()

        content = topic_page.content
        title = content.get_title()

        self.assertIn(self.__START_CREATE_TOPIC_PAGE_TITLE, title)

        blog_description = content.get_blog_description

        self.assertIn(self.__START_BLOG_DESCRIPTION_TITLE, blog_description.get_title())
        self.assertIn(self.__START_BLOG_DESCRIPTION, blog_description.get_description())

        form = content.get_form
        blog_name = form.get_blog_name()
        topic_header = form.get_topic_header()

        self.assertIn(self.__START_BLOG_NAME, blog_name)
        self.assertFalse(topic_header)


    def tearDown(self):
        super(TopicCreationTestCase, self).tearDown()
