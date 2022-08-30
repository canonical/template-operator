# Copyright {{ year }} {{ author }}
# See LICENSE file for licensing details.

import unittest

from ops.model import ActiveStatus
from ops.testing import Harness

from charm import {{ class_name }}


class TestCharm(unittest.TestCase):
    def setUp(self):
        self.harness = Harness({{ class_name }})
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()
    
    def test_pebble_ready(self):
        # Simulate the container coming up and emission of pebble-ready event
        self.harness.container_pebble_ready("some-container")
        # Ensure we set an ActiveStatus with no message
        self.assertEqual(self.harness.model.unit.status, ActiveStatus())
