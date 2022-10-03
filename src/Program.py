#!/usr/bin/python3
import threading
from LoggerModule import *
from TCPServer import *
from _global import *

LOGGINGINIT()

try:
      from LCDController import *
except Exception as ex:
    LOGEVENTS_ERROR(f"{ex}")
    
if (__name__ == '__main__'):
    
    try:
        LCDINIT()
    except Exception as ex:
        LOGEVENTS_ERROR(f"{ex}")
        
    try:
        threading.Thread(target=LCDROUTINE).start()
    except Exception as ex:
        LOGEVENTS_ERROR(f"{ex}")
        LOGEVENTS_INFO("Ignore above errors if LCD module has not been installed due to lack of an LCD screen on/or connected to the hardware")
        LOGEVENTS_INFO("Ensure sys.path.append(DIR HERE) has been set in LCDController.py to match driver installation directory")
    
    TCPSRVMAIN()

else:
    LOGEVENTS_ERROR("Attempted code execution from an indirect source")
    LOGEVENTS_CRITICAL(f"Terminating NET-RMSI_Srv_Py")
    quit(code=1)
    





    
    


    