#!/usr/bin/python3
import threading
from LoggerModule import *
from LCDController import *
from TCPServer import *


#Change this value dependant if server hardware has a compatible LCD screen
lcdmoduleenabled = False


global serverversion = "001"



if (lcdmoduleenabled == True and __name__ == '__main__'):
    LCDINIT()
    LOGGINGINIT()
    task0 = threading.Thread(target=LOGGINGINIT)
    task0.start()
    task0.join()

    TCPSRVMAIN()

    
elif(__name__ == '__main__'):
    LOGGINGINIT()
    TCPSRVMAIN()

else:
    LOGEVENTS_ERROR("Attempted code execution from an indirect source")
    LOGEVENTS_CRITICAL(f"Terminating NET-RMSI_Srv_Py")
    quit()
    





    
    


    