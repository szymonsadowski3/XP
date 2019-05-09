from persistence.DatabaseAccess import DatabaseAccess


class UserRegistrationService:
    def __init__(self, repository=DatabaseAccess()):
        self.repository = repository

    def add_user(self, user_to_add):
        self.repository.add_user(user_to_add)

    def get_all_users(self):
        return self.repository.get_all_users()

    def get_user_by_username(self, username):
        return self.repository.get_user_by_username(username)

    def remove_user(self, username_of_user_to_remove):
        self.repository.remove_user(username_of_user_to_remove)
