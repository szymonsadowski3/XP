import time


def get_current_date():
    return "%04u-%02u-%02uT%02u:%02u:%02u" % time.localtime(time.time())[0:6]
