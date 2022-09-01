#!/usr/bin/python3
import TCPServer, LCDController
from TCPServer import tcpconstatus

#Passthrough global vars required for vertification and data processing
from TCPServer import data
from TCPServer import conaddress

from LCDController import lcdmoduleenabled



if (lcdmoduleenabled == True):
    LCDController.LCDINIT()
    TCPServer.TCPSRVINIT()
else:
    TCPServer.TCPSRVINIT()

while(lcdmoduleenabled == True):
    if(TCPServer.TCPSRVINIT == True):
        LCDController.LCDConnectiontrue()
        TCPServer.TCPDATACOLLECTION()
    elif(TCPServer.TCPSRVINIT == False):
        print(f"{tcpconstatus}")
        LCDController.LCDConnectionfalse()


    
    


    