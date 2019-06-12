import sys
import os
import time

from src.utils.utils import get_current_date

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from persistence.MicroDatabaseAccess import MicroDatabaseAccess
from models.Log import Log
import unittest


class TestMicroDatabaseAccessLogsOperations(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMicroDatabaseAccessLogsOperations, self).__init__(*args, **kwargs)
        self.database_access = None

    def setUp(self):
        self.database_access = MicroDatabaseAccess()

    def test_adding_log(self):
        log_message = "This is sample message"
        info_log_level = Log.log_levels[1]
        source = "TestMicroDatabaseAccessLogsOperations.class"

        self.database_access.add_log(log_message, info_log_level, source)
        logs = self.database_access.get_all_logs()
        added_log = logs[0]
        self.assertEqual(added_log.message, log_message)
        self.assertEqual(added_log.level, info_log_level)
        self.assertEqual(added_log.source, source)

    def test_searching_log_by_level(self):
        source = "TestMicroDatabaseAccessLogsOperations.class"
        other_logs = [
            ("This is sample message 0", Log.log_levels[1], source),
            ("This is sample message 1", Log.log_levels[1], source),
        ]

        level_0_logs = [
            ("This is sample message 2", Log.log_levels[0], source),
            ("This is sample message 3", Log.log_levels[0], source)
        ]

        for log_message, info_log_level, source in other_logs:
            self.database_access.add_log(log_message, info_log_level, source)

        for log_message, info_log_level, source in level_0_logs:
            self.database_access.add_log(log_message, info_log_level, source)

        logs = self.database_access.get_all_logs_by_level(Log.log_levels[0])

        self.assertEqual(logs, level_0_logs)

    def test_searching_log_by_source(self):
        source1 = "source1"
        source2 = "source2"

        source1_logs = [
            ("This is sample message 0", Log.log_levels[1], source1),
            ("This is sample message 1", Log.log_levels[1], source1),
        ]

        source2_logs = [
            ("This is sample message 2", Log.log_levels[0], source2),
            ("This is sample message 3", Log.log_levels[0], source2)
        ]

        for log_message, info_log_level, source in source1_logs:
            self.database_access.add_log(log_message, info_log_level, source)

        for log_message, info_log_level, source in source2_logs:
            self.database_access.add_log(log_message, info_log_level, source)

        logs = self.database_access.get_all_logs_by_source(source2)

        self.assertEqual(logs, source2_logs)

    def test_searching_log_by_time_range(self):
        source = "TestMicroDatabaseAccessLogsOperations.class"

        batch1_logs = [
            ("This is sample message 0", Log.log_levels[1], source),
            ("This is sample message 1", Log.log_levels[1], source),
        ]

        batch2_logs = [
            ("This is sample message 2", Log.log_levels[0], source),
            ("This is sample message 3", Log.log_levels[0], source)
        ]

        insert1_timestamp = get_current_date()

        for log_message, info_log_level, source in batch1_logs:
            self.database_access.add_log(log_message, info_log_level, source)

        time.sleep(3)

        insert2_timestamp = get_current_date()

        for log_message, info_log_level, source in batch2_logs:
            self.database_access.add_log(log_message, info_log_level, source)

        logs = self.database_access.get_all_logs_by_time_range(insert1_timestamp, insert2_timestamp)
        self.assertEqual(logs, batch1_logs)


if __name__ == '__main__':
    unittest.main()
