import time

class Client:
    def __init__(self, name, time_offset):
        self.name = name
        self.time_offset = time_offset

    def get_current_time(self):
        local_time = time.localtime()
        minutes = int(local_time.tm_hour) * 60 + int(local_time.tm_min) + self.time_offset
        hours = minutes // 60
        minutes = minutes % 60
        return hours, minutes

 
