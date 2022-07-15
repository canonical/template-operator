# Copyright {{ year }} {{ author }}
# See LICENSE file for licensing details.

import unittest

from ops.testing import Harness

from charm import {{ class_name }}


class TestCharm(unittest.TestCase):
    def setUp(self):
        self.harness = Harness({{ class_name }})
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()
    
    def test_something(self):
        self.assertTrue(True)