import unittest

from models.User import User
from persistence.DatabaseAccess import DatabaseAccess


class TestUserRegistration(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.database_access = None

    def setUp(self):
        self.database_access = DatabaseAccess()

    def test_adding_to_db(self):
        user_to_add = User("szymon", 0)

        self.database_access.add_user(user_to_add)

        user_from_database = self.database_access.get_user_by_username("szymon")

        self.assertEqual(user_to_add.username, user_from_database.username)
        self.assertEqual(user_to_add.card_id, user_from_database.card_id)

    def test_querying_missing_user_returns_none(self):
        returnValue = self.database_access.get_user_by_username("admin")
        self.assertEqual(returnValue, None)

    def test_returns_user(self):
        testUser = User("admin", 0)
        self.database_access.add_user(testUser)
        returnedUser = self.database_access.get_user_by_username("admin")
        self.assertEqual(testUser, returnedUser)

    def test_returns_empty_list_when_empty(self):
        self.assertEqual([], self.database_access.get_all_users())

    def test_returns_all_users_when_not_empty(self):
        firstUser = User("admin", 0)
        secondUser = User("mrowka", 1)
        self.database_access.add_user(firstUser)
        self.database_access.add_user(secondUser)
        response = self.database_access.get_all_users()
        self.assertEqual(response, [firstUser, secondUser])

    def test_compiler_sanity(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()