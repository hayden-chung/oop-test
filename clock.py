import time
import os 

# define properties & actions of clock

def sec_counter(hr, min, sec, alrm_time):
    while sec < 60:
        print(f'{hr} hr, {min} min, {sec} seconds')
        if (hr, min, sec) == alrm_time:
            print("ringringringringring")
            time.sleep(10)
        time.sleep(0.001)
        sec += 1
        os.system('cls')
    sec = 0
    return sec

def min_counter(hr, min, sec, alrm_time):
    while min < 60:
        sec = sec_counter(hr, min, sec, alrm_time)
        min += 1
    min = 0
    return min

def hr_counter(hr, min, sec, alrm_time):
    while hr < 24:
        min = min_counter(hr, min, sec, alrm_time)
        hr += 1
    


class Clock():
    def __init__(self, hr, min, sec):
        self.hr = hr
        self.min = min
        self.sec = 0
        self.alrm_time = (None, None, None)

    def start(self):
        hr_counter(self.hr, self.min, self.sec, self.alrm_time)
    
    def alarm(self, alrm_time):
        hr_counter(self.hr, self.min, self.sec, alrm_time)
        











myclock = Clock(1, 0, 0)

# myclock.start()

myclock.alarm((1, 2, 29))

