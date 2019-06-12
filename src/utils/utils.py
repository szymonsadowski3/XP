import utime


def get_current_date():
    return "%04u-%02u-%02uT%02u:%02u:%02u" % utime.localtime(utime.time())[0:6]
