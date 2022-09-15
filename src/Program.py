#!/usr/bin/python3
import TCPServer, LCDController, LoggerModule


#Change this value dependant if server hardware has a compatible LCD screen
lcdmoduleenabled = True



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


    
    


    