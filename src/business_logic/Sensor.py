
import time
import _thread
from datetime import datetime
from business_logic.LogSaver import LogSaver
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")



def get_current_date():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class Sensor:

    def __fallback_system(self):
        while True:
            if self.emergency_state == True:
                self.is_door_open = True
            time.sleep(0.1)

    def __init__(self, room_id):
        self.room_id = room_id
        self.log_saver = LogSaver()
        self.emergency_thread = _thread.start_new_thread(self.__fallback_system)
        self.is_door_open = False
        self.emergency_state = False

    def __unlock_door():
        self.is_door_open = True

    def __close_door():
        if self.emergency_state:
            pass

        self.is_door_open = False

    def open(self, card_obj):
        if check_in(card_obj):
            __unlock_door()

    def check_in(self, card_obj):
        is_access_granted = self.room_id in card_obj.accessible_room_ids
        self.log_saver.send_log(
            get_current_date(),
            "AccessGranted?={0} for room_id={1} and card_id={2}".format(
                is_access_granted, self.room_id, card_obj.card_id
            )
        )
        return is_access_granted

    def check_out(self):
        pass
