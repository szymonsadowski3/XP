import random
import string

from models.User import User


class TestUtils:
    current_user_id = 0

    @classmethod
    def get_next_user(cls):
        username = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        user = User(username, TestUtils.current_user_id)
        TestUtils.current_user_id += 1
        return user
