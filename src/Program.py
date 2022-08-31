#!/usr/bin/python3
from pickle import TRUE
import TCPServer, LCDController
from TCPServer import tcpconstatus
from LCDController import LCDMODULEENABLED



if (LCDMODULEENABLED == TRUE):
    LCDController.LCDINIT()
    TCPServer.TCPSRVINIT()
else:
    TCPServer.TCPSRVINIT()

while(LCDMODULEENABLED == TRUE):
    if(tcpconstatus == TRUE):
        LCDController.LCDConnectiontrue()
    elif(tcpconstatus == False):
        print(f"{tcpconstatus}")
        LCDController.LCDConnectionfalse()


    
    


    