import time

class Server:
    def __init__(self):
        pass

    def get_current_time(self):
        local_time = time.localtime()
        return local_time.tm_hour, local_time.tm_min

