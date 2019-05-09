from peewee import *

from src.persistence.DbObject import db_object


class Card(Model):
    card_id = AutoField()

    class Meta:
        database = db_object


class Room(Model):
    room_id = AutoField()
    card_id = ForeignKeyField(Card, backref='accessible_rooms')

    class Meta:
        database = db_object


class User(Model):
    username = CharField()
    card_id = AutoField()

    class Meta:
        database = db_object