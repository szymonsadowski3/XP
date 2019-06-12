class BaseDoorLock:

    def unlock(self):
        pass

    def lock(self):
        pass

class MockedDoorLock(BaseDoorLock):

    def __init__(self):
        self.is_locked = True

    def unlock(self):
        if self.is_locked:
            self.is_locked = False

    def lock(self):
        if not self.is_locked:
            self.is_locked = True