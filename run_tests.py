#!/usr/bin/env python2

import unittest
from tests.authorization_test import AuthorizationTestCase


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthorizationTestCase),
    ))
    unittest.TextTestRunner().run(suite)
