# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from tests import Component, POLLING_TIME, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN


__author__ = 'a.halaidzhy'


class ResultContent(Component):
    __CONTENT_BLOCK = '//div[@id="content"]'
    __STATUS_MESSAGE = __CONTENT_BLOCK + '//ul[contains(@class, "system-message-notice")]/li[1]'
    __HEADER_BLOCK = __CONTENT_BLOCK + '//header[contains(@class, "topic-header")]'
    __LATEST_LIST = '//ul[contains(@class, "latest-list")]'
    __LATEST_TOPIC = __LATEST_LIST + '/li[1]'
    __LATEST_TOPIC_AUTHOR = __LATEST_TOPIC + '//a[contains(@class, "author")]'
    __LATEST_TOPIC_BLOG = __LATEST_TOPIC + '//a[contains(@class, "stream-blog")]'
    __LATEST_TOPIC_TITLE = __LATEST_TOPIC + '//a[contains(@class, "stream-topic")]'
    __TOPIC_TITLE = __HEADER_BLOCK + '//h1[contains(@class, "topic-title")]/a[1]'
    __TOPIC_INFO = __HEADER_BLOCK + '//a[contains(@class, "topic-blog")]'
    __ACTION_EDIT = __HEADER_BLOCK + '//a[contains(@class, "actions-edit")]'
    __ACTION_DELETE = __HEADER_BLOCK + '//a[contains(@class, "actions-delete")]'
    __POLL_BLOCK = __CONTENT_BLOCK + '//div[contains(@class, "poll")]'
    __POLL_ANSWERS = __POLL_BLOCK + '//ul[contains(@class, "poll-vote")]//input[contains(@class, "answer")]'
    __VOTE_BUTTON = __POLL_BLOCK + '//button[contains(@class, "vote")]'
    __ABSTAIN_BUTTON = __POLL_BLOCK + '//button[contains(@class, "abstain")]'
    __TOPIC_CONTENT = __CONTENT_BLOCK + '//div[contains(@class, "topic-content")]/p[1]'
    __TOPIC_FOOTER_BLOCK = __CONTENT_BLOCK + '//footer[contains(@class, "topic-footer")]'
    __TOPIC_AUTHOR = __TOPIC_FOOTER_BLOCK + '//a[@rel="author"]'
    __TOPIC_FAVOURITE = __TOPIC_FOOTER_BLOCK + '//span[contains(@class, "favourite-count")]'
    __TOPIC_VOTE_COUNT = __TOPIC_FOOTER_BLOCK + '//div[contains(@class, "vote-count")]'
    __TOPIC_COMMENTS_COUNT = '//span[@id="count-comments"]'
    __TOPIC_COMMENT_SUBSCRIBE = '//input[@id="comment_subscribe"]'
    __COMMENT_ADD_ELEMENT = __CONTENT_BLOCK + '//a[contains(@class, "comment-add-link")]'
    __DRAFT_TOPIC = __CONTENT_BLOCK + '//i[contains(@class, "icon-synio-topic-draft")]'
    __LEFT_BLOCK = __CONTENT_BLOCK + '//div[contains(@class, "feed-left")]'

    def get_latest_topic(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__LATEST_TOPIC)
        )
        latest_topic_author = self.driver.find_element_by_xpath(self.__LATEST_TOPIC_AUTHOR).text
        latest_topic_blog = self.driver.find_element_by_xpath(self.__LATEST_TOPIC_BLOG).text
        latest_topic_title = self.driver.find_element_by_xpath(self.__LATEST_TOPIC_TITLE).text
        return {
            'author': latest_topic_author,
            'blog': latest_topic_blog,
            'title': latest_topic_title
        }

    def get_status_message(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__STATUS_MESSAGE)
        )
        return self.driver.find_element_by_xpath(self.__STATUS_MESSAGE).text

    def get_topic_title(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TOPIC_TITLE)
        )
        return self.driver.find_element_by_xpath(self.__TOPIC_TITLE).text

    def press_edit_topic(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__ACTION_EDIT)
        )
        self.driver.find_element_by_xpath(self.__ACTION_EDIT).click()

    def press_delete_topic(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__ACTION_DELETE)
        )
        self.driver.find_element_by_xpath(self.__ACTION_DELETE).click()

    def get_poll_form_answers(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_elements_by_xpath(self.__POLL_ANSWERS)
        )
        poll_answers = self.driver.find_elements_by_xpath(self.__POLL_ANSWERS)
        result_list = []
        for answer in poll_answers:
            result_list.append(answer.text)
        return result_list

    def get_vote_button_text(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__VOTE_BUTTON)
        )
        return self.driver.find_element_by_xpath(self.__VOTE_BUTTON).text

    def get_abstain_button_text(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__ABSTAIN_BUTTON)
        )
        return self.driver.find_element_by_xpath(self.__ABSTAIN_BUTTON).text

    def get_topic_content(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TOPIC_CONTENT)
        )
        return self.driver.find_element_by_xpath(self.__TOPIC_CONTENT).text

    def get_topic_info(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TOPIC_FOOTER_BLOCK)
        )
        topic_author = self.driver.find_element_by_xpath(self.__TOPIC_AUTHOR).text
        topic_favourite = self.driver.find_element_by_xpath(self.__TOPIC_FAVOURITE).text
        topic_vote_count = self.driver.find_element_by_xpath(self.__TOPIC_VOTE_COUNT).text
        return {
            'author': topic_author,
            'favourite': topic_favourite,
            'vote_count': topic_vote_count
        }

    def get_subscribe_status(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TOPIC_COMMENT_SUBSCRIBE)
        )
        return self.driver.find_element_by_xpath(self.__TOPIC_COMMENT_SUBSCRIBE).is_selected()

    def is_add_comment_link_present(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__LEFT_BLOCK)
        )
        try:
            self.driver.find_element_by_xpath(self.__COMMENT_ADD_ELEMENT)
            return True
        except NoSuchElementException:
            return False

    def is_in_draft(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__TOPIC_TITLE)
        )
        try:
            self.driver.find_element_by_xpath(self.__DRAFT_TOPIC)
            return True
        except NoSuchElementException:
            return False
