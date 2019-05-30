from peewee import *

from src.models.Models import Card, Room, User
from src.persistence.DbObject import db_object


class DatabaseAccessSqlite:
    def __init__(self):
        self.db = db_object
        db_object.create_tables([
            Card,
            Room,
            User
        ])

    def add_card(self):
        return Card.create()

    def add_user(self, username):
        card_for_user = self.add_card()
        user = User.create(username=username, card_id=card_for_user.card_id)
        user.save()

    def get_user_by_username(self, username):
        query = (User
                 .select()
                 .where(User.username == username))

        records = list(query)

        return records[0] if len(records) > 0 else None

    def get_all_users(self):
        return list(User.select())
    #
    # def remove_user(self, username_of_user_to_remove):
    #     self.users = [user for user in self.users if user.username != username_of_user_to_remove]
    #
    def clear_database(self):
        delete_query = Card.delete()
        delete_query.execute()
        delete_query = Room.delete()
        delete_query.execute()
        delete_query = User.delete()
        delete_query.execute()

