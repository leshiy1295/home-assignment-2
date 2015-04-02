# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait

from tests import Component, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME
from tests.topic_creation.page_and_component_objects.blog_description import BlogDescription
from tests.topic_creation.page_and_component_objects.create_topic_form import CreateTopicForm


__author__ = 'a.halaidzhy'


class Content(Component):
    __TITLE_ELEMENT = '//div[@id="content"]//h2[contains(@class, "page-header")]'
    __TOPIC = '//article'
    __TOPIC_TITLE = '//h1[contains(@class, "topic-title")]/a[1]'
    __TOPIC_AUTHOR = '//a[@rel="author"]'

    def get_title(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TITLE_ELEMENT)
        )
        return self.driver.find_element_by_xpath(self.__TITLE_ELEMENT).text

    @property
    def get_form(self):
        return CreateTopicForm(self.driver)

    @property
    def get_blog_description(self):
        return BlogDescription(self.driver)

    def topic_exists(self, topic_info):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_elements_by_xpath(self.__TOPIC)
        )
        last_topics = self.driver.find_elements_by_xpath(self.__TOPIC)
        found = False
        for topic in last_topics:
            topic_title = topic.find_element_by_xpath(self.__TOPIC_TITLE).text
            topic_author = topic.find_element_by_xpath(self.__TOPIC_AUTHOR).text
            if topic_author == topic_info['author'] and topic_title == topic_info['title']:
                found = True
                break
        return found
