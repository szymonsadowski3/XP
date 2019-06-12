from src.models.User import User


class MicroDatabaseAccess:
    def __init__(self):
        self.users = []

    def add_user(self, username_to_add, is_admin=False):
        return None

    def get_user_by_username(self, username):
        return None

    def get_user_by_id(self, identifier):
        return None

    def remove_user_by_username(self, username_of_user_to_remove):
        return None

    def remove_user_by_id(self, id_of_user_to_remove):
        return None

    def get_all_users(self):
        return None

    def get_all_admins(self):
        return None

    def change_admin_rights_by_id(self, user_id, should_user_be_admin_now):
        return None
