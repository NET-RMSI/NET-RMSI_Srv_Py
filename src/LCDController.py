#!/usr/bin/python3
import socket
import sys
from _global import *
from time import sleep
#Enter location of LCD drivers directory
sys.path.append('/home/kitt/lcd/')
import drivers

lcddisplay = drivers.Lcd()

HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(HOSTNAME)

def LCDINIT():
    lcddisplay.lcd_display_string("NET-RMSI_SRV", 1)
    lcddisplay.lcd_display_string(f"IP: {IP}", 2)
    
    
def LCDROUTINE():
    while True:
        sleep(4)
        lcddisplay.lcd_clear()
        lcddisplay.lcd_display_string("NET-RMSI_SRV", 1)
        lcddisplay.lcd_display_string(f"{serverversion}", 2)
        sleep(4)
        lcddisplay.lcd_clear()
        lcddisplay.lcd_display_string("NET-RMSI_SRV", 1)
        lcddisplay.lcd_display_string(f"IP: {IP}", 2)
        sleep(4)
        lcddisplay.lcd_clear()
        lcddisplay.lcd_display_string("NET-RMSI_SRV", 1)
        lcddisplay.lcd_display_string(f"{serverversion}", 2)
        sleep(4)
        lcddisplay.lcd_clear()
        lcddisplay.lcd_display_string("NET-RMSI_SRV", 1)
        lcddisplay.lcd_display_string(f"IP: {IP}", 2)












