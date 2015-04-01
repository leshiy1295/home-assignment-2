# -*- coding: utf-8 -*-
from time import sleep

import urlparse
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


__author__ = 'a.halaidzhy'

MAXIMUM_WAIT_TIME_FOR_JS = 10
MAXIMUM_WAIT_TIME_FOR_PAGE_OPEN = 30
POLLING_TIME = 0.1


class SeleniumTest(unittest.TestCase):
    __HUB_URL = 'http://127.0.0.1:4444/wd/hub'
    __BROWSER = os.environ.get('TTHA2BROWSER', 'FIREFOX')

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=self.__HUB_URL,
            desired_capabilities=getattr(DesiredCapabilities, self.__BROWSER).copy()
        )

    def tearDown(self):
        sleep(3) # Time for manual validation of final test result
        self.driver.quit()


class Page(object):
    BASE_URL = 'http://ftest.stud.tech-mail.ru/'
    __PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.__PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Component(object):
    def __init__(self, driver):
        self.driver = driver
