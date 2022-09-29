#!/usr/bin/python3
import socket
#Enter location of LCD drivers directory
sys.path.append('/home/kitt/lcd/')
import drivers

lcddisplay = drivers.Lcd()


def LCDINIT():
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












