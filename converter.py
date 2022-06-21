import os 
import sys
from telnetlib import X3PAD 
import json
from numba import njit,prange
import math 
import random 
import calendar
import datetime 

def open_file(x,mode):
    if mode == 1 or mode == 2:
        f = open(x)
        data = json.load(f)
    if mode == 1:
        return [data[x] for x in range(0,len(data)) if data[x].get("bannerType") == "WEAPON"]
    elif mode == 2:
        return [data[x] for x in range(0,len(data)) if data[x].get("bannerType") == "EVENT"]



class Change_Value():

    def __init__(self):
        self.curr_time = calendar.timegm((datetime.datetime.utcnow()).timetuple())
        print(self.curr_time)
        self.change_values_char(open_file("Banners.json",2),1)
        print("Ready!")

    def change_values_char(self,x,mode):
        minutes = 30
        self.prev_x = x
        self.ch = x
        #for x in range(2):
            #for x in range(0,len(self.ch)):
                    #self.ch.append(self.ch[x])
        if mode != 1:
            for x in self.ch:
                future = calendar.timegm((datetime.datetime.fromtimestamp(self.curr_time)  + datetime.timedelta(minutes=int(minutes))).timetuple())
                x["beginTime"] = self.curr_time
                x["endTime"] = future
                self.curr_time = calendar.timegm((datetime.datetime.fromtimestamp(self.curr_time)  + datetime.timedelta(minutes=int(minutes))).timetuple())
                minutes += 30
            with open("Banner3.json","w") as of:
                json.dump(self.ch,of,indent=2)
        else:
            for x in self.ch:
                future = calendar.timegm((datetime.datetime.fromtimestamp(self.curr_time)  + datetime.timedelta(minutes=int(minutes))).timetuple())
                x["beginTime"] = self.curr_time
                x["endTime"] = future
                self.curr_time = calendar.timegm((datetime.datetime.fromtimestamp(self.curr_time)  + datetime.timedelta(minutes=int(minutes))).timetuple())
                minutes += 30
            self.final_banner = self.ch + self.prev_x
            with open("Banner3.json","w") as of:
                json.dump(self.final_banner,of,indent=2)

            


    

Change_Value()
