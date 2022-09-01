#!/usr/bin/python3
from pickle import TRUE
import sys
from time import time
import socket


sys.path.append('/home/kitt/lcd/')
import drivers

lcddisplay = drivers.Lcd()


def LCDINIT():
    global lcdmoduleenabled
    lcdmoduleenabled = False

    HOSTNAME = socket.gethostname()
    IP = socket.gethostbyname(HOSTNAME)
    lcddisplay.lcd_display_string("NET-RMSI_SRV", 1)
    lcddisplay.lcd_display_string(f"IP: {IP}", 2)
    
def LCDConnectiontrue():
    lcddisplay.lcd_display_string("NET-RMSI_SRV", 1)
    lcddisplay.lcd_display_string("Cli Connected", 2)

def LCDConnectionfalse():
    lcddisplay.lcd_display_string("NET-RMSI_SRV", 1)
    lcddisplay.lcd_display_string("No Connection", 2)












