from persistence.DatabaseAccess import DatabaseAccess
from models.User import User
import unittest
import sys
import os
from src.business_logic import Sensor
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")


class TestSensor(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSensor, self).__init__(*args, **kwargs)
        self.sensor = None

    def setUp(self):
        self.sensor = Sensor()

    def test_sensor_fallback(self):
        self.sensor.emergency_state = True
        for i in range(5):
            if self.sensor.is_door_open:
                pass
            time.sleep(0.1)
        self.fail("Door hasn't opened")

if __name__ == '__main__':
    unittest.main()
