#!/usr/bin/python3
import TCPServer, LCDController, LoggerModule


#Change this value dependant if server hardware has a compatible LCD screen
lcdmoduleenabled = True



if (lcdmoduleenabled == True):
    LCDController.LCDINIT()
    LoggerModule.LOGGINGINIT()
    TCPServer.TCPSRVMAIN()
    
else:
    LoggerModule.LOGGINGINIT()
    TCPServer.TCPSRVMAIN()


while(lcdmoduleenabled == True):
    if(TCPServer.TCPSRVMAIN == True):
        LCDController.LCDConnectiontrue()
        TCPServer.TCPDATACOLLECTION()
    elif(TCPServer.TCPSRVINIT == False):
        LCDController.LCDConnectionfalse()


    
    


    