import sys
import os

from src.persistence.DatabaseAccessSqlite import DatabaseAccessSqlite

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import unittest
import string
import random


class TestUtils:
    current_user_id = 0

    @classmethod
    def get_random_username(cls):
        username = ''.join(random.choice(
            string.ascii_uppercase + string.digits) for _ in range(10))
        return username


class TestDatabaseAccess(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDatabaseAccess, self).__init__(*args, **kwargs)
        self.database_access = None

    def setUp(self):
        self.database_access = DatabaseAccessSqlite()

    def test_adding_to_db(self):
        random_username = TestUtils.get_random_username()

        self.database_access.add_user(random_username)

        user_from_database = self.database_access.get_user_by_username(random_username)

        self.assertEqual(random_username, user_from_database.username)

    def test_querying_missing_user_returns_none(self):
        returnValue = self.database_access.get_user_by_username("SomeUser")
        self.assertEqual(returnValue, None)

    def test_returns_user(self):
        testUser = TestUtils.get_random_username()
        self.database_access.add_user(testUser)
        returnedUser = self.database_access.get_user_by_username(
            testUser.username)
        self.assertEqual(testUser, returnedUser)

    def test_returns_empty_list_when_empty(self):
        self.database_access.clear_database()
        self.assertEqual([], self.database_access.get_all_users())

    def test_returns_all_users_when_not_empty(self):
        first_user = TestUtils.get_random_username()
        second_user = TestUtils.get_random_username()
        self.database_access.add_user(first_user)
        self.database_access.add_user(second_user)
        response = self.database_access.get_all_users()
        self.assertEqual(response, [first_user, second_user])

    def test_clear_database(self):
        user_to_add = TestUtils.get_random_username()
        self.database_access.add_user(user_to_add)
        self.database_access.clear_database()
        self.assertEqual([], self.database_access.get_all_users())

    def test_remove_user(self):
        user_to_add = TestUtils.get_random_username()
        username = user_to_add.username
        self.database_access.add_user(user_to_add)
        self.database_access.remove_user(username)
        returnValue = self.database_access.get_user_by_username(username)
        self.assertEqual(returnValue, None)


if __name__ == '__main__':
    unittest.main()
