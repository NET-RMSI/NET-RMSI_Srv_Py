#!/usr/bin/python3
from _global import *
from time import sleep
import rpi_lcd

lcddisplay = rpi_lcd.LCD()

def LCDINIT():
    lcddisplay.text("NET-RMSI_SRV", 1)
    lcddisplay.text(f"IP: {IPADDRESS}", 2)
    
    
def LCDROUTINE():
    while True:
        sleep(4)
        lcddisplay.clear()
        lcddisplay.text("NET-RMSI_SRV", 1)
        lcddisplay.text(f"{serverversion}", 2)
        sleep(4)
        lcddisplay.clear()
        lcddisplay.text("NET-RMSI_SRV", 1)
        lcddisplay.text(f"IP: {IPADDRESS}", 2)
        sleep(4)
        lcddisplay.clear()
        lcddisplay.text("NET-RMSI_SRV", 1)
        lcddisplay.text(f"{serverversion}", 2)
        sleep(4)
        lcddisplay.clear()
        lcddisplay.text("NET-RMSI_SRV", 1)
        lcddisplay.text(f"IP: {IPADDRESS}", 2)












