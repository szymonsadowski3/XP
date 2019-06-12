import time


def get_current_date():
    return "%04u-%02u-%02uT%02u:%02u:%02u" % time.localtime(utime.time())[0:6]
