import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from persistence.DatabaseAccess import DatabaseAccess
from models.User import User
import unittest
import string
import random


class TestUtils:
    current_user_id = 0

    @classmethod
    def get_next_user(cls):
        username = ''.join(random.choice(
            string.ascii_uppercase + string.digits) for _ in range(10))
        user = User(username, TestUtils.current_user_id)
        TestUtils.current_user_id += 1
        return user


class TestDatabaseAccess(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDatabaseAccess, self).__init__(*args, **kwargs)
        self.database_access = None

    def setUp(self):
        self.database_access = DatabaseAccess()

    def test_adding_to_db(self):
        user_to_add = TestUtils.get_next_user()

        self.database_access.add_user(user_to_add)

        user_from_database = self.database_access.get_user_by_username(
            user_to_add.username)

        self.assertEqual(user_to_add.username, user_from_database.username)
        self.assertEqual(user_to_add.card_id, user_from_database.card_id)

    def test_querying_missing_user_returns_none(self):
        return_value = self.database_access.get_user_by_username("SomeUser")
        self.assertEqual(return_value, None)

    def test_returns_user(self):
        test_user = TestUtils.get_next_user()
        self.database_access.add_user(test_user)
        returned_user = self.database_access.get_user_by_username(
            test_user.username)
        self.assertEqual(test_user, returned_user)

    def test_returns_empty_list_when_empty(self):
        self.database_access.clear_database()
        self.assertEqual([], self.database_access.get_all_users())

    def test_returns_all_users_when_not_empty(self):
        first_user = TestUtils.get_next_user()
        second_user = TestUtils.get_next_user()
        self.database_access.add_user(first_user)
        self.database_access.add_user(second_user)
        response = self.database_access.get_all_users()
        self.assertEqual(response, [first_user, second_user])

    def test_clear_database(self):
        user_to_add = TestUtils.get_next_user()
        self.database_access.add_user(user_to_add)
        self.database_access.clear_database()
        self.assertEqual([], self.database_access.get_all_users())

    def test_remove_user(self):
        user_to_add = TestUtils.get_next_user()
        username = user_to_add.username
        self.database_access.add_user(user_to_add)
        self.database_access.remove_user(username)
        return_value = self.database_access.get_user_by_username(username)
        self.assertEqual(return_value, None)


if __name__ == '__main__':
    unittest.main()
