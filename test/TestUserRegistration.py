import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import unittest

from models.User import User
from business_logic.UserRegistrationService import UserRegistrationService


class TestUserRegistration(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestUserRegistration, self).__init__(*args, **kwargs)
        self.userRegistrationService = None

    def setUp(self):
        self.userRegistrationService = UserRegistrationService()

    def test_adding_to_db(self):
        user_to_add = User("szymon", 0)

        self.userRegistrationService.add_user(user_to_add)

        user_from_database = self.userRegistrationService.get_user_by_username("szymon")

        self.assertEqual(user_to_add.username, user_from_database.username)
        self.assertEqual(user_to_add.card_id, user_from_database.card_id)

    def test_querying_missing_user_returns_none(self):
        returnValue = self.userRegistrationService.get_user_by_username("admin")
        self.assertEqual(returnValue, None)

    def test_returns_user(self):
        testUser = User("admin", 0)
        self.userRegistrationService.add_user(testUser)
        returnedUser = self.userRegistrationService.get_user_by_username("admin")
        self.assertEqual(testUser.username, returnedUser.username)
        self.assertEqual(testUser.card_id, returnedUser.card_id)

    def test_returns_empty_list_when_empty(self):
        self.userRegistrationService.repository.clear_database()
        self.assertEqual([], self.userRegistrationService.get_all_users())

    def test_returns_all_users_when_not_empty(self):
        self.userRegistrationService.repository.clear_database()
        firstUser = User("admin", 0)
        secondUser = User("mrowka", 1)
        self.userRegistrationService.add_user(firstUser)
        self.userRegistrationService.add_user(secondUser)
        response = self.userRegistrationService.get_all_users()
        self.assertEqual(response, [firstUser, secondUser])

    def test_compiler_sanity(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
