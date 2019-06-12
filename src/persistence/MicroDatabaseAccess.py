import time

from models.Log import Log
from models.User import User

class MicroDatabaseAccess:
    id_sequence_current_value = 1

    def __init__(self, admin_list=[]):
        self.users = []
        self.logs = []
        for admin in admin_list:
            if isinstance(admin, User):
                self.users.append(admin)

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
        log_to_add = Log(message, level, source)
        self.logs.append(log_to_add)

    def get_all_logs(self):
        return self.logs

    def get_all_logs_by_level(self, level):
        return [log for log in self.logs if log.level == level]

    def get_all_logs_by_source(self, source):
        return [log for log in self.logs if log.source == source]

    # def get_all_logs_by_time_range(self, timestamp1, timestamp2):
    #     dt1 = datetime.datetime.strptime(timestamp1, default_date_time_format)
    #     dt2 = datetime.datetime.strptime(timestamp2, default_date_time_format)

    #     return [
    #         log for log in self.logs
    #         if dt1 <= datetime.datetime.strptime(log.timestamp, default_date_time_format) <= dt2
    #     ]
