import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from persistence.MicroDatabaseAccess import MicroDatabaseAccess
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


class TestMicroDatabaseAccessUsersOperations(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestMicroDatabaseAccessUsersOperations, self).__init__(*args, **kwargs)
        self.database_access = None

    def setUp(self):
        self.database_access = MicroDatabaseAccess()

    def test_adding_to_db(self):
        username_of_user_to_add = "szymon"

        assigned_id = self.database_access.add_user(username_of_user_to_add)

        user_from_database_by_username = self.database_access.get_user_by_username("szymon")
        user_from_database_by_id = self.database_access.get_user_by_id(assigned_id)

        self.assertEqual(username_of_user_to_add, user_from_database_by_username.username)
        self.assertEqual(username_of_user_to_add, user_from_database_by_id.username)
        self.assertEqual(user_from_database_by_username, user_from_database_by_id)

    def test_querying_missing_user_returns_none(self):
        self.database_access.remove_user_by_username("SomeUser")
        return_value = self.database_access.get_user_by_username("SomeUser")
        self.assertEqual(return_value, None)

    def test_removing_user_by_username(self):
        username_of_user_to_add = "szymon"
        assigned_id = self.database_access.add_user(username_of_user_to_add)
        self.assertEqual(self.database_access.get_user_by_id(assigned_id).username, username_of_user_to_add)

        self.database_access.remove_user_by_username(username_of_user_to_add)

        self.assertEqual(self.database_access.get_user_by_id(assigned_id), None)

    def test_removing_user_by_id(self):
        username_of_user_to_add = "szymon"
        assigned_id = self.database_access.add_user(username_of_user_to_add)
        self.assertEqual(self.database_access.get_user_by_id(assigned_id).username, username_of_user_to_add)

        self.database_access.remove_user_by_id(assigned_id)

        self.assertEqual(self.database_access.get_user_by_id(assigned_id), None)

    def test_adding_admin_to_db(self):
        username_of_user_to_add = "szymon"

        assigned_id = self.database_access.add_user(username_of_user_to_add, is_admin=True)

        user_from_database = self.database_access.get_user_by_id(assigned_id)

        self.assertTrue(user_from_database.is_admin)

    def test_getting_all_users(self):
        usernames_to_add = ["szymon", "zbigniew", "roza"]

        assigned_ids = [self.database_access.add_user(username, is_admin=False) for username in usernames_to_add]

        users_from_database = [self.database_access.get_user_by_id(assigned_id) for assigned_id in assigned_ids]

        all_users = self.database_access.get_all_users()

        self.assertEqual(all_users, users_from_database)

        for user_from_db, username in zip(all_users, usernames_to_add):
            self.assertEqual(username, user_from_db.username)

    def test_getting_all_users_when_no_users_in_db(self):
        self.database_access.users = []
        self.assertEqual([], self.database_access.get_all_users())

    def test_getting_all_admins(self):
        usernames_to_add = ["szymon", "zbigniew", "roza"]
        admins_to_add = ["maciej", "franciszek"]

        [self.database_access.add_user(username, is_admin=False) for username in usernames_to_add]

        assigned_admin_ids = [
            self.database_access.add_user(admin_username, is_admin=True) for admin_username in admins_to_add
        ]

        admins_from_database = [self.database_access.get_user_by_id(assigned_id) for assigned_id in assigned_admin_ids]

        all_admins = self.database_access.get_all_admins()
        self.assertEqual(all_admins, admins_from_database)

        for admin_from_db, username in zip(all_admins, admins_to_add):
            self.assertEqual(username, admin_from_db.username)
            self.assertTrue(username, admin_from_db.is_admin)

    def test_changing_admin_rights(self):
        username_of_user_to_add = "szymon"

        assigned_id = self.database_access.add_user(username_of_user_to_add)

        user_from_database_by_id = self.database_access.get_user_by_id(assigned_id)
        self.assertFalse(user_from_database_by_id.is_admin)

        self.database_access.change_admin_rights_by_id(assigned_id, should_user_be_admin_now=True)

        self.assertTrue(user_from_database_by_id.is_admin)


if __name__ == '__main__':
    unittest.main()
