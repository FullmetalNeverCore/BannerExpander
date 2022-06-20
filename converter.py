import os 
import sys 
import ujson
from numba import njit,prange
import math 
import random 


def open_file(x):
    f = open(x)
    data = ujson.load(f)
    return [data[x] for x in range(0,len(data)) if data[x].get("bannerType") == "WEAPON"],[data[x] for x in range(0,len(data)) if data[x].get("bannerType") == "EVENT"]




class Change_Value():

    def __init__(self,char,weap):
        self.initial_time = 1659999922
        self.initial_weapon_time = 1659999922
        self.ch = char
        self.wp = weap
        for x in range(1,8):
            for x in range(0,len(self.ch)):
                self.ch.append(self.ch[x])
            for x in range(0,len(self.wp)):
                self.ch.append(self.wp[x])
        self.event_banner = self.change_values_char()
        self.weapon_banner = self.change_values_weap()
        self.final_banner_list = self.event_banner+self.weapon_banner
        self.write_file(self.event_banner+self.weapon_banner)

    def change_values_char(self):
        print(len(self.ch))
        print("START CHAR")
        #waeaponbanner = [data_object[x] for x in range(0,len(data_object)) if data_object[x].get("bannerType") == "WEAPON"]
        for x in range(0,len(self.ch)):
                self.ch[x].update(beginTime=int(self.initial_time),endTime=int(self.initial_time+1000))
                #chosen_weapon = random.choice(waeaponbanner)
                #data_object.append(chosen_weapon)
                self.initial_time = self.initial_time + 1000
                print(str(self.initial_time) + "Char")
        #initial_time = 1650661019
        #for x in range(0,len(data_object)):
            #if(data_object[x].get("bannerType") == "WEAPON"):
               # data_object[x].update(beginTime=int(initial_time),endTime=int(initial_time+1000))
               # initial_time += 1000

        #print(data_object)
        return self.ch
    
    def change_values_weap(self):
        print(len(self.wp))
        print("START WEAPON")
        for x in range(0,len(self.wp)):
            if(self.wp[x].get("bannerType") == "WEAPON"):
                self.wp[x].update(beginTime=int(self.initial_weapon_time),endTime=int(self.initial_weapon_time+1000))
                self.initial_weapon_time = self.initial_weapon_time + 1000
        return self.wp
    
    def write_file(self,x):
        with open('Banner3.json', 'w') as outfile:outfile.write(ujson.dumps(x,indent=2))


x,y = open_file("Banners.json")
Change_Value(x,y)