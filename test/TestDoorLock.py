import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from business_logic.doorlock import MockedDoorLock
import unittest
import string
import random

class TestDoorLock(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDoorLock, self).__init__(*args, **kwargs)
        self.lock = None

    def setUp(self):
        self.lock = MockedDoorLock()

    def test_door_open_by_default(self):
        pass
    
    def test_door_opens(self):
        pass

    def test_door_closes(self):
        pass

    
    


if __name__ == '__main__':
    unittest.main()
