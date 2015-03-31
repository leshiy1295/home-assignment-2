# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait

from tests import Component

__author__ = 'a.halaidzhy'


class TopMenu(Component):
    USERNAME = u'Лизонька Манилова'
    _USERNAME_ELEMENT = '//div[@id="dropdown-user"]//a[contains(@class, "username")]'

    def get_username(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self._USERNAME_ELEMENT).text
        )
