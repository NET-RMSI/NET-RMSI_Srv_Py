#!/usr/bin/python3
import ipaddress
import TCPServer
import drivers

lcddisplay = drivers.LCD()

def LCDStandby():
    ip = ipaddress.IPv4Address
    while True:
        lcddisplay.lcd_display_string("NET-RMSI_SRV", 1)
        lcddisplay.lcd_display_string("IP: {ip}", 2)





