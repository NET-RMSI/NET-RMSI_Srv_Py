#!/usr/bin/python3
import TCPServer, LCDController, LoggerModule

#Passthrough global vars required for vertification and data processing
from LCDController import lcdmoduleenabled



if (lcdmoduleenabled == True):
    LCDController.LCDINIT()
    LoggerModule.LOGGINGINIT()
    TCPServer.TCPSRVINIT()
    
else:
    LoggerModule.LOGGINGINIT()
    TCPServer.TCPSRVINIT()


while(lcdmoduleenabled == True):
    if(TCPServer.TCPSRVINIT == True):
        LCDController.LCDConnectiontrue()
        TCPServer.TCPDATACOLLECTION()
    elif(TCPServer.TCPSRVINIT == False):
        LCDController.LCDConnectionfalse()


    
    


    