#!/usr/bin/python3
import sys
from TCPServer import tcpconstatus
import socket

sys.path.append('/home/kitt/lcd/')
import drivers

lcddisplay = drivers.Lcd()

def LCDStandby():
    HOSTNAME = socket.gethostname()
    IP = socket.gethostbyname(HOSTNAME)
    while tcpconstatus == False:
        lcddisplay.lcd_display_string("NET-RMSI_SRV", 1)
        lcddisplay.lcd_display_string(f"IP: {IP}", 2)





