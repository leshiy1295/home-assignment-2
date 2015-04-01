from tests import Page
from tests.topic_creation.page_and_component_objects.result_content import ResultContent

__author__ = 'a.halaidzhy'


class ResultPage(Page):

    @property
    def content(self):
        return ResultContent(self.driver)
