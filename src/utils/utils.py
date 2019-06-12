from datetime import datetime

from src.utils.constants import default_date_time_format


def get_current_date():
    return datetime.now().strftime(default_date_time_format)


class DatetimeRange:
    def __init__(self, dt1, dt2):
        self.dt1 = dt1
        self.dt2 = dt2

    def __contains__(self, dt):

        if self.dt1 < dt < self.dt2:
            return True
        else:
            return False
