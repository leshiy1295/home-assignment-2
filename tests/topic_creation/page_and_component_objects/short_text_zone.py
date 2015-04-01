# -*- coding: utf-8 -*-

from tests.topic_creation.page_and_component_objects.text_zone import TextZone

__author__ = 'a.halaidzhy'


class ShortTextZone(TextZone):
    __LABEL_FOR_ZONE = '//label[@for="id_text"]'
    __TEXTAREA_ELEMENT = '//textarea[@id="id_text"]'
