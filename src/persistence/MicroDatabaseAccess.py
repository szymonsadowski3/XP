from src.models.User import User


class MicroDatabaseAccess:
    id_sequence_current_value = 0

    def __init__(self):
        self.users = []
        self.logs = []

    def add_user(self, username_to_add, is_admin=False):
        id_to_assign = MicroDatabaseAccess.id_sequence_current_value
        user_to_add = User(username_to_add, id_to_assign, is_admin)
        self.users.append(user_to_add)
        MicroDatabaseAccess.id_sequence_current_value += 1
        return id_to_assign

    def get_user_by_username(self, username):
        filtered_users = [user for user in self.users if user.username == username]

        return filtered_users[0] if (len(filtered_users) > 0) else None

    def get_user_by_id(self, identifier):
        filtered_users = [user for user in self.users if user.user_id == identifier]

        return filtered_users[0] if (len(filtered_users) > 0) else None

    def remove_user_by_username(self, username_of_user_to_remove):
        self.users = [user for user in self.users if user.username != username_of_user_to_remove]

    def remove_user_by_id(self, id_of_user_to_remove):
        self.users = [user for user in self.users if user.user_id != id_of_user_to_remove]

    def get_all_users(self):
        return self.users

    def get_all_admins(self):
        return [user for user in self.users if user.is_admin]

    def change_admin_rights_by_id(self, user_id, should_user_be_admin_now):
        user = self.get_user_by_id(user_id)
        user.is_admin = should_user_be_admin_now

    def add_log(self, message, level=None, source=None):
        pass

    def get_all_logs(self):
        pass

    def get_all_logs_by_level(self, level):
        pass

    def get_all_logs_by_source(self, source):
        pass

    def get_all_logs_by_time_range(self, timestamp1, timestamp2):
        pass
