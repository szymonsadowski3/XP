from business_logic.LogSaver import LogSaver
from utils.utils import get_current_date


class Sensor:
    def __init__(self, room_id):
        self.room_id = room_id
        self.log_saver = LogSaver()

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

