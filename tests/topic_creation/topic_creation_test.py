# -*- coding: utf-8 -*-

import os
from time import sleep

from tests import SeleniumTest
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
    __SIMPLE_POLL_QUESTION = u'Хорошо ли быть тестировщиком?'
    __SIMPLE_POLL_ANSWER_0 = u'Да ";)<script>alert(1)</script>'
    __SIMPLE_POLL_ANSWER_1 = u'Нет ;(" and 1 = 1 -- comment'
    __SIMPLE_POLL_ANSWER_2 = u'Затрудняюсь ответить \'"o_O"\''
    __LARGE_TOPIC_HEADER = u'Просто топик с длинным названием - wow' * 10
    __LARGE_SHORT_TEXT = u'Длинный текст для простого топика' * 10
    __LARGE_TEXT = u'Длинный текст для простого топика' * 100
    __ERROR_LABEL_LARGE_HEADER_TEXT = u'Убедитесь, что это значение содержит не более 250 символов'
    __MAX_TOPIC_HEADER = u'X' * 250
    __LARGE_LAST_TOPIC = {
        'author': TopMenu.USERNAME,
        'blog': CreateTopicForm.BLOG_NAME,
        'title': __MAX_TOPIC_HEADER
    }
    __BOLD_EFFECT = u'****'
    __BOLD_TEST_INPUT = u'**Жирный текст**'
    __BOLD_TEST_ASSERT = u'Жирный текст'

    __ITALIC_EFFECT = u'**'
    __ITALIC_TEST_INPUT = u'*Курсив*'
    __ITALIC_TEST_ASSERT = u'Курсив'

    __QUOTE_EFFECT = u'> '
    __QUOTE_TEST = u'Цитата'

    __UNORDERED_LIST_EFFECT = u'* '
    __UNORDERED_LIST_TEST = u'Элемент ненумерованного списка'

    __ORDERED_LIST_EFFECT = u'1. '
    __ORDERED_LIST_TEST = u'Элемент нумерованного списка'

    def setUp(self):
        super(TopicCreationTestCase, self).setUp()
        AuthPage(self.driver).log_in()
        self.__topic_page = TopicCreationPage(self.driver)
        self.__topic_page.open()
        self.should_remove = False

    def test_start_state_of_page(self):
        content = self.__topic_page.content
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

    def test_submit_without_any_data(self):
        form = self.__topic_page.content.get_form
        form.submit_form()

        checkbox_zone = form.get_checkbox_zone
        checkbox_zone.open_poll()

        self.assertIn(self.__ERROR_LABEL_TEXT, form.get_blog_name_error())
        self.assertIn(self.__ERROR_LABEL_TEXT, form.get_topic_header_error())
        self.assertIn(self.__ERROR_LABEL_TEXT, form.get_short_text_zone.get_error_label())
        self.assertIn(self.__ERROR_LABEL_TEXT, form.get_text_zone.get_error_label())
        self.assertIn(self.__ERROR_LABEL_TEXT, checkbox_zone.get_error_label())

    def test_correct_simple_form_and_check_of_all_fields_on_result_page_with_manual_remove(self):
        form = self.__topic_page.content.get_form
        form.click_on_select_blog_name()
        form.set_blog_name()

        self.assertIn(self.__CORRECT_SIMPLE_BLOG_DESCRIPTION,
                      self.__topic_page.content.get_blog_description.get_description())

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

    def test_with_poll_with_3_answers_in_drafts_without_comments(self):
        form = self.__topic_page.content.get_form

        form.click_on_select_blog_name()
        form.set_blog_name()
        form.set_topic_header(self.__CORRECT_SIMPLE_TOPIC_HEADER)

        short_text_zone = form.get_short_text_zone
        text_zone = form.get_text_zone
        checkbox_zone = form.get_checkbox_zone

        short_text_zone.set_text(self.__CORRECT_SIMPLE_SHORT_TEXT)
        text_zone.set_text(self.__CORRECT_SIMPLE_TEXT)
        checkbox_zone.open_poll()
        checkbox_zone.set_poll_question(self.__SIMPLE_POLL_QUESTION)
        self.assertEqual(checkbox_zone.get_poll_answers_count(), 2)
        checkbox_zone.set_poll_answer_with_number(0, self.__SIMPLE_POLL_ANSWER_0)
        checkbox_zone.set_poll_answer_with_number(1, self.__SIMPLE_POLL_ANSWER_1)
        checkbox_zone.add_poll_answer()
        checkbox_zone.set_poll_answer_with_number(2, self.__SIMPLE_POLL_ANSWER_2)
        checkbox_zone.remove_poll_answer()
        self.assertEqual(checkbox_zone.get_poll_answers_count(), 2)
        checkbox_zone.add_poll_answer()
        checkbox_zone.set_poll_answer_with_number(2, self.__SIMPLE_POLL_ANSWER_2)
        self.assertEqual(checkbox_zone.get_poll_answers_count(), 3)

        checkbox_zone.set_publish_element_status(False)
        checkbox_zone.set_forbid_element_status(True)

        form.submit_form()

        self.should_remove = True
        self.__published_topic_page = ResultPage(self.driver)
        result_page_content = self.__published_topic_page.content
        topic_info = result_page_content.get_topic_info()
        poll_form_answers_count = result_page_content.get_poll_form_answers_count()

        self.assertEqual(poll_form_answers_count, 3)
        self.assertIn(self.__CORRECT_SIMPLE_SUCCESS_STATUS_MESSAGE, result_page_content.get_status_message())
        self.assertIn(self.__CORRECT_SIMPLE_TOPIC_HEADER, result_page_content.get_topic_title())
        self.assertIn(self.__CORRECT_SIMPLE_TEXT, result_page_content.get_topic_content())
        for key in self.__CORRECT_SIMPLE_TOPIC_INFO:
            self.assertIn(self.__CORRECT_SIMPLE_TOPIC_INFO[key], topic_info[key])
        self.assertTrue(result_page_content.get_subscribe_status())
        self.assertFalse(result_page_content.is_add_comment_link_present())
        self.assertTrue(result_page_content.is_in_draft())

    def test_large_texts(self):
        form = self.__topic_page.content.get_form
        form.click_on_select_blog_name()
        form.set_blog_name()

        self.assertIn(self.__CORRECT_SIMPLE_BLOG_DESCRIPTION,
                      self.__topic_page.content.get_blog_description.get_description())

        form.set_topic_header(self.__LARGE_TOPIC_HEADER)
        short_text_zone = form.get_short_text_zone
        short_text_zone.set_text(self.__LARGE_SHORT_TEXT)
        text_zone = form.get_text_zone
        text_zone.set_text(self.__LARGE_TEXT)
        form.submit_form()

        self.assertIn(self.__ERROR_LABEL_LARGE_HEADER_TEXT, form.get_topic_header_error())

        form.set_topic_header(self.__MAX_TOPIC_HEADER)
        form.submit_form()

        self.should_remove = True
        self.__published_topic_page = ResultPage(self.driver)
        result_page_content = self.__published_topic_page.content
        latest_topic = result_page_content.get_latest_topic()
        topic_info = result_page_content.get_topic_info()

        for key in self.__LARGE_LAST_TOPIC:
            self.assertIn(self.__LARGE_LAST_TOPIC[key], latest_topic[key])
        self.assertIn(self.__CORRECT_SIMPLE_SUCCESS_STATUS_MESSAGE, result_page_content.get_status_message())
        self.assertIn(self.__MAX_TOPIC_HEADER, result_page_content.get_topic_title())
        self.assertIn(self.__LARGE_TEXT, result_page_content.get_topic_content())
        for key in self.__CORRECT_SIMPLE_TOPIC_INFO:
            self.assertIn(self.__CORRECT_SIMPLE_TOPIC_INFO[key], topic_info[key])
        self.assertTrue(result_page_content.get_subscribe_status())
        self.assertTrue(result_page_content.is_add_comment_link_present())
        self.assertFalse(result_page_content.is_in_draft())

    def test_bold_element(self):
        form = self.__topic_page.content.get_form

        text_area = form.get_text_zone
        text_area.trigger_bold_tool()
        self.assertIn(self.__BOLD_EFFECT, text_area.get_text())

    def test_bold_with_preview(self):
        form = self.__topic_page.content.get_form
        form.click_on_select_blog_name()
        form.set_blog_name()

        form.set_topic_header(self.__CORRECT_SIMPLE_TOPIC_HEADER)
        form.get_short_text_zone.set_text(self.__CORRECT_SIMPLE_SHORT_TEXT)

        text_area = form.get_text_zone

        text_area.set_text(self.__BOLD_TEST_INPUT)
        text_area.trigger_preview_tool()
        self.assertIn(self.__BOLD_TEST_ASSERT, text_area.get_bold_text_from_preview_editor())

        form.submit_form()

        self.should_remove = True
        self.__published_topic_page = ResultPage(self.driver)
        result_page_content = self.__published_topic_page.content

        self.assertIn(self.__BOLD_TEST_ASSERT, result_page_content.get_bold_topic_content())

    def test_italic_element(self):
        form = self.__topic_page.content.get_form

        text_area = form.get_text_zone
        text_area.trigger_italic_tool()
        self.assertIn(self.__ITALIC_EFFECT, text_area.get_text())

    def test_italic_with_preview(self):
        form = self.__topic_page.content.get_form
        form.click_on_select_blog_name()
        form.set_blog_name()

        form.set_topic_header(self.__CORRECT_SIMPLE_TOPIC_HEADER)
        form.get_short_text_zone.set_text(self.__CORRECT_SIMPLE_SHORT_TEXT)

        text_area = form.get_text_zone

        text_area.set_text(self.__ITALIC_TEST_INPUT)
        text_area.trigger_preview_tool()
        self.assertIn(self.__ITALIC_TEST_ASSERT, text_area.get_italic_text_from_preview_editor())

        form.submit_form()

        self.should_remove = True
        self.__published_topic_page = ResultPage(self.driver)
        result_page_content = self.__published_topic_page.content

        self.assertIn(self.__ITALIC_TEST_ASSERT, result_page_content.get_italic_topic_content())

    def test_quote_with_preview(self):
        form = self.__topic_page.content.get_form
        form.click_on_select_blog_name()
        form.set_blog_name()

        form.set_topic_header(self.__CORRECT_SIMPLE_TOPIC_HEADER)
        form.get_short_text_zone.set_text(self.__CORRECT_SIMPLE_SHORT_TEXT)

        text_area = form.get_text_zone

        text_area.trigger_quote_tool()
        self.assertIn(self.__QUOTE_EFFECT, text_area.get_text())

        text_area.set_text(self.__QUOTE_TEST)
        text_area.trigger_preview_tool()
        self.assertIn(self.__QUOTE_TEST, text_area.get_quote_text_from_preview_editor())

        form.submit_form()

        self.should_remove = True
        self.__published_topic_page = ResultPage(self.driver)
        result_page_content = self.__published_topic_page.content

        self.assertIn(self.__QUOTE_EFFECT + self.__QUOTE_TEST, result_page_content.get_topic_content())

    def test_unordered_list_with_preview(self):
        form = self.__topic_page.content.get_form
        form.click_on_select_blog_name()
        form.set_blog_name()

        form.set_topic_header(self.__CORRECT_SIMPLE_TOPIC_HEADER)
        form.get_short_text_zone.set_text(self.__CORRECT_SIMPLE_SHORT_TEXT)

        text_area = form.get_text_zone

        text_area.trigger_unordered_list_tool()
        self.assertIn(self.__UNORDERED_LIST_EFFECT, text_area.get_text())

        text_area.set_text(self.__UNORDERED_LIST_TEST)
        text_area.trigger_preview_tool()
        self.assertIn(self.__UNORDERED_LIST_TEST, text_area.get_unordered_list_text_from_preview_editor())

        form.submit_form()

        self.should_remove = True
        self.__published_topic_page = ResultPage(self.driver)
        result_page_content = self.__published_topic_page.content

        self.assertIn(self.__UNORDERED_LIST_TEST, result_page_content.get_unordered_list_topic_content())

    def test_ordered_list_with_preview(self):
        form = self.__topic_page.content.get_form
        form.click_on_select_blog_name()
        form.set_blog_name()

        form.set_topic_header(self.__CORRECT_SIMPLE_TOPIC_HEADER)
        form.get_short_text_zone.set_text(self.__CORRECT_SIMPLE_SHORT_TEXT)

        text_area = form.get_text_zone

        text_area.trigger_ordered_list_tool()
        self.assertIn(self.__ORDERED_LIST_EFFECT, text_area.get_text())

        text_area.set_text(self.__ORDERED_LIST_TEST)
        text_area.trigger_preview_tool()
        self.assertIn(self.__ORDERED_LIST_TEST, text_area.get_ordered_list_text_from_preview_editor())

        form.submit_form()

        self.should_remove = True
        self.__published_topic_page = ResultPage(self.driver)
        result_page_content = self.__published_topic_page.content

        self.assertIn(self.__ORDERED_LIST_TEST, result_page_content.get_ordered_list_topic_content())

    def tearDown(self):
        if self.should_remove:
            self.__published_topic_page.remove()
        super(TopicCreationTestCase, self).tearDown()
