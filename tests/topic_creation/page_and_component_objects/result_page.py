from tests import Page
from tests.topic_creation.page_and_component_objects.result_content import ResultContent
from tests.topic_creation.page_and_component_objects.topic_deletion_page import TopicDeletionPage

__author__ = 'a.halaidzhy'


class ResultPage(Page):

    @property
    def content(self):
        return ResultContent(self.driver)

    def remove(self):
        self.content.press_delete_topic()
        delete_page = TopicDeletionPage(self.driver)
        delete_page.press_delete_button()
