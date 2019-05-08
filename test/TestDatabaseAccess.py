import random
import string
import unittest

from models.User import User
from persistence.DatabaseAccess import DatabaseAccess


class TestUtils:
    current_user_id = 0

    @classmethod
    def get_next_user(cls):
        username = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        user = User(username, TestUtils.current_user_id)
        TestUtils.current_user_id += 1
        return user


class TestDatabaseAccess(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.database_access = None

    def setUp(self):
        self.database_access = DatabaseAccess()

    def test_adding_to_db(self):
        user_to_add = TestUtils.get_next_user()

        self.database_access.add_user(user_to_add)

        user_from_database = self.database_access.get_user_by_username(user_to_add.username)

        self.assertEqual(user_to_add.username, user_from_database.username)
        self.assertEqual(user_to_add.card_id, user_from_database.card_id)

    def test_querying_missing_user_returns_none(self):
        returnValue = self.database_access.get_user_by_username("SomeUser")
        self.assertEqual(returnValue, None)

    def test_returns_user(self):
        testUser = TestUtils.get_next_user()
        self.database_access.add_user(testUser)
        returnedUser = self.database_access.get_user_by_username(testUser.username)
        self.assertEqual(testUser, returnedUser)

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
        returnValue = self.database_access.get_user_by_username(username)
        self.assertEqual(returnValue, None)


if __name__ == '__main__':
    unittest.main()
