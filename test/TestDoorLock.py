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
        self.door_lock = None

    def setUp(self):
        self.door_lock = MockedDoorLock()

    def test_door_open_by_default(self):
        self.assertTrue(self.door_lock.is_locked)
    
    def test_door_unlock(self):
        self.door_lock.is_locked = True
        self.door_lock.unlock()
        self.assertFalse(self.door_lock.is_locked)

    def test_door_lock(self):
        self.door_lock.is_locked = False
        self.door_lock.lock()
        self.assertTrue(self.door_lock.is_locked)


    
    


if __name__ == '__main__':
    unittest.main()
