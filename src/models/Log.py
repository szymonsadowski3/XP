from utils.utils import get_current_date


class Log:
    log_levels = ["DEBUG", "INFO", "ERROR"]

    def __init__(self, message, level=None, source=None, timestamp=None):
        self.message = message

        self.level = Log.log_levels[0] if level is None else level
        self.source = "root" if source is None else source
        self.timestamp = get_current_date() if timestamp is None else timestamp
