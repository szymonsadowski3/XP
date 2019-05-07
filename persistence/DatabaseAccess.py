class DatabaseAccess:
    def __init__(self):
        self.users = []
        self.cards = []

    def add_user(self, user_to_add):
        self.users.append(user_to_add)

    def get_all_users(self):
        return self.users

    def get_user_by_username(self, username):
        filtered_users = [user for user in self.users if user.username==username]

        return filtered_users[0] if (len(filtered_users) > 0) else None

    def remove_user(self, username_of_user_to_remove):
        self.users = [user for user in self.users if user.username != username_of_user_to_remove]

    def clear_database(self):
        self.users = []
        self.cards = []

