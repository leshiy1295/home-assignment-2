#!/usr/bin/env python2

import unittest

from tests.authorization.authorization_test import AuthorizationTestCase
from tests.redirects_to_topic_creation.redirects_test import RedirectsTestCase
from tests.topic_creation.topic_creation_test import TopicCreationTestCase


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthorizationTestCase),
        unittest.makeSuite(RedirectsTestCase),
        unittest.makeSuite(TopicCreationTestCase),
    ))
    unittest.TextTestRunner().run(suite)
