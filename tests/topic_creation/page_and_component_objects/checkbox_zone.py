# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait

from tests import Component, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME, MAXIMUM_WAIT_TIME_FOR_JS

__author__ = 'a.halaidzhy'


class CheckBoxZone(Component):
    __FORM_ELEMENT = '//div[@id=content]//form'
    __ADD_POLL_ELEMENT = __FORM_ELEMENT + '//input[@name="add_poll"]'
    __PUBLISH_ELEMENT = '//input[@id="id_publish"]'
    __FORBID_ELEMENT = '//input[@id="id_forbid_comment"]'
    __POLL_QUESTION = '//input[@id="id_question"]'
    __ADD_POLL_ANSWER = __FORM_ELEMENT + '//a[contains(@class, "add-poll-answer")]'
    __REMOVE_POLL_ANSWER = __FORM_ELEMENT + '//a[contains(@class, "remove-poll-answer")]'
    __QUESTION_LIST = '//ul[@id="question_list"]'

    def __get_poll_answer_path_with_number(self, number):
        return '//input[@id="id_form-{}-answer"]'.format(number)

    def open_poll(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__ADD_POLL_ELEMENT)
        )
        add_poll_checkbox = self.driver.find_element_by_xpath(self.__ADD_POLL_ELEMENT)
        if not add_poll_checkbox.is_selected():
            add_poll_checkbox.click()

    def get_poll_question(self):
        return WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__POLL_QUESTION).text
        )

    def set_poll_question(self, question):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__POLL_QUESTION)
        )
        self.driver.find_element_by_xpath(self.__POLL_QUESTION).send_keys(question)

    def get_poll_answer_with_number(self, number):
        return WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__get_poll_answer_path_with_number(number)).text
        )

    def get_poll_answers_count(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__QUESTION_LIST)
        )
        question_list = self.driver.find_element_by_xpath(self.__QUESTION_LIST)
        poll_answers = question_list.find_elements_by_tag_name('li')
        return len(poll_answers)

    def set_poll_answer_with_number(self, number, answer):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__get_poll_answer_path_with_number(number))
        )
        self.driver.find_element_by_xpath(self.__get_poll_answer_path_with_number(number)).send_keys(answer)

    def add_poll_answer(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__ADD_POLL_ANSWER)
        )
        self.driver.find_element_by_xpath(self.__ADD_POLL_ANSWER).click()

    def remove_poll_answer(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__REMOVE_POLL_ANSWER)
        )
        self.driver.find_element_by_xpath(self.__REMOVE_POLL_ANSWER).click()

    def close_poll(self):
        WebDriverWait(self.driver, MAXIMUM_WAIT_TIME_FOR_JS, POLLING_TIME).until(
            lambda d: d.find_element_by_xpath(self.__ADD_POLL_ELEMENT)
        )
        add_poll_checkbox = self.driver.find_element_by_xpath(self.__ADD_POLL_ELEMENT)
        if add_poll_checkbox.is_selected():
            add_poll_checkbox.click()
