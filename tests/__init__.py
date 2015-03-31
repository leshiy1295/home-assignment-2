# -*- coding: utf-8 -*-

import urlparse

__author__ = 'a.halaidzhy'


class Page(object):
    BASE_URL = 'http://ftest.stud.tech-mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Component(object):
    def __init__(self, driver):
        self.driver = driver
