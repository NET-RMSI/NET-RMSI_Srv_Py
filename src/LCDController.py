#!/usr/bin/python3
from socket import gethostname
import TCPServer
import drivers

lcddisplay = drivers.LCD()

def LCDStandby():
    ip = gethostname()
    while True:
        lcddisplay.lcd_display_string("NET-RMSI_SRV", 1)
        lcddisplay.lcd_display_string("IP: {ip}", 2)



