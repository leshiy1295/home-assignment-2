# -*- coding: utf-8 -*-

import os

from tests import SeleniumTest, dont_remove_topic
from tests.authorization.page_and_component_objects.auth_page import AuthPage
from tests.redirects_to_topic_creation.page_and_component_objects.portal_main_page import PortalMainPage
from tests.redirects_to_topic_creation.page_and_component_objects.top_menu import TopMenu
from tests.topic_creation.page_and_component_objects.create_topic_form import CreateTopicForm
from tests.topic_creation.page_and_component_objects.result_page import ResultPage
from tests.topic_creation.page_and_component_objects.topic_creation_page import TopicCreationPage


__author__ = 'a.halaidzhy'


class TopicCreationTestCase(SeleniumTest):
    __PATH_TO_IMAGE = os.path.dirname(__file__) + '/res/image.jpg'
    __START_CREATE_TOPIC_PAGE_TITLE = u'Создание топика'
    __START_BLOG_DESCRIPTION_TITLE = u'Описание блога'
    __START_BLOG_DESCRIPTION = u'Выберите блог'
    __START_BLOG_NAME = u'-' * 9
    __EMPTY_STRING = u''
    __START_STRING_FOR_TEXT = u' '
    __ERROR_LABEL_TEXT = u'Это поле обязательно для заполнения.'
    __CORRECT_SIMPLE_BLOG_DESCRIPTION = u'Блог для общих топиков'
    __CORRECT_SIMPLE_TOPIC_HEADER = u'Просто топик с обычным названием - wow'
    __CORRECT_SIMPLE_SHORT_TEXT = u'Обычный текст для простого топика'
    __CORRECT_SIMPLE_TEXT = u'Обычный текст для простого топика' * 10
    __CORRECT_SIMPLE_LAST_TOPIC = {
        'author': TopMenu.USERNAME,
        'blog': CreateTopicForm.BLOG_NAME,
        'title': __CORRECT_SIMPLE_TOPIC_HEADER
    }
    __CORRECT_SIMPLE_SUCCESS_STATUS_MESSAGE = u'Топик успешно создан'
    __CORRECT_SIMPLE_TOPIC_INFO = {
        'author': TopMenu.USERNAME,
        'favourite': "0",
        'vote_count': "0.0"
    }

    def setUp(self):
        super(TopicCreationTestCase, self).setUp()
        AuthPage(self.driver).log_in()
        self.should_remove = True

    @dont_remove_topic
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
        self.assertEqual(topic_header, self.__EMPTY_STRING)

        short_text_zone = form.get_short_text_zone
        text_zone = form.get_text_zone
        checkbox_zone = form.get_checkbox_zone

        short_text = short_text_zone.get_text()
        text = text_zone.get_text()
        add_poll_element_checked = checkbox_zone.get_poll_add_element_status()
        publish_element_checked = checkbox_zone.get_publish_element_status()
        forbid_element_checked = checkbox_zone.get_forbid_status()

        self.assertEqual(short_text, self.__START_STRING_FOR_TEXT)
        self.assertEqual(text, self.__START_STRING_FOR_TEXT)
        self.assertFalse(add_poll_element_checked)
        self.assertTrue(publish_element_checked)
        self.assertFalse(forbid_element_checked)

    @dont_remove_topic
    def test_submit_without_any_data(self):
        topic_page = TopicCreationPage(self.driver)
        topic_page.open()

        form = topic_page.content.get_form
        form.submit_form()

        checkbox_zone = form.get_checkbox_zone
        checkbox_zone.open_poll()

        self.assertIn(self.__ERROR_LABEL_TEXT, form.get_blog_name_error())
        self.assertIn(self.__ERROR_LABEL_TEXT, form.get_topic_header_error())
        self.assertIn(self.__ERROR_LABEL_TEXT, form.get_short_text_zone.get_error_label())
        self.assertIn(self.__ERROR_LABEL_TEXT, form.get_text_zone.get_error_label())
    #     self.assertIn(self.__ERROR_LABEL_TEXT, checkbox_zone.get_error_label())

    @dont_remove_topic
    def test_correct_simple_form_and_check_of_all_fields_on_result_page_with_manual_remove(self):
        topic_page = TopicCreationPage(self.driver)
        topic_page.open()

        form = topic_page.content.get_form
        form.click_on_select_blog_name()
        form.set_blog_name()

        self.assertIn(self.__CORRECT_SIMPLE_BLOG_DESCRIPTION, topic_page.content.get_blog_description.get_description())

        form.set_topic_header(self.__CORRECT_SIMPLE_TOPIC_HEADER)
        short_text_zone = form.get_short_text_zone
        short_text_zone.set_text(self.__CORRECT_SIMPLE_SHORT_TEXT)
        text_zone = form.get_text_zone
        text_zone.set_text(self.__CORRECT_SIMPLE_TEXT)
        form.submit_form()

        published_topic_page = ResultPage(self.driver)
        result_page_content = published_topic_page.content
        latest_topic = result_page_content.get_latest_topic()
        topic_info = result_page_content.get_topic_info()

        for key in self.__CORRECT_SIMPLE_LAST_TOPIC:
            self.assertIn(self.__CORRECT_SIMPLE_LAST_TOPIC[key], latest_topic[key])
        self.assertIn(self.__CORRECT_SIMPLE_SUCCESS_STATUS_MESSAGE, result_page_content.get_status_message())
        self.assertIn(self.__CORRECT_SIMPLE_TOPIC_HEADER, result_page_content.get_topic_title())
        self.assertIn(self.__CORRECT_SIMPLE_TEXT, result_page_content.get_topic_content())
        for key in self.__CORRECT_SIMPLE_TOPIC_INFO:
            self.assertIn(self.__CORRECT_SIMPLE_TOPIC_INFO[key], topic_info[key])
        self.assertTrue(result_page_content.get_subscribe_status())
        self.assertTrue(result_page_content.is_add_comment_link_present())
        self.assertFalse(result_page_content.is_in_draft())

        published_topic_page.remove()

        main_page = PortalMainPage(self.driver)
        self.assertTrue(main_page.is_topic_removed(latest_topic))

    def tearDown(self):
        if self.should_remove:
            self.published_topic_page.remove()
        super(TopicCreationTestCase, self).tearDown()
