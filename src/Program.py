#!/usr/bin/python3
import TCPServer, LCDController
from TCPServer import tcpconstatus
from LCDController import LCDMODULEENABLED



if (LCDMODULEENABLED == True):
    LCDController.LCDINIT()
    TCPServer.TCPSRVINIT()
else:
    TCPServer.TCPSRVINIT()

while(LCDMODULEENABLED == True):
    if(tcpconstatus == True):
        LCDController.LCDConnectiontrue()
    elif(tcpconstatus == False):
        print(f"{tcpconstatus}")
        LCDController.LCDConnectionfalse()


    
    


    