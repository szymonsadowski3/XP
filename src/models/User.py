class User:
    def __init__(self, username, card_id):
        self.username = username
        self.card_id = card_id

    def __eq__(self, obj):
        return isinstance(obj, User) and obj.username == self.username and self.card_id == obj.card_id
