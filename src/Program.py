#!/usr/bin/python3
import threading
from EventLogging import *
from TCPServer import *
from _global import *

    
if (__name__ == '__main__'):

#Start logging.
    LoggingInit()
    
    try:
        from LCDController import *
        LCDINIT()
        threading.Thread(target=LCDROUTINE).start()
    except Exception as ex:
        LOGEVENTS_ERROR(f"{ex}")
        LOGEVENTS_INFO("Ignore above errors if LCD module has not been installed due to lack of an LCD screen on/or connected to the hardware")
    
    TCPServer(IPADDRESS, PORT).TCPServerinit()

else:
    LOGEVENTS_ERROR("Attempted code execution from an indirect source")
    LOGEVENTS_CRITICAL(f"Terminating NET-RMSI_Srv_Py")
    quit(code=1)
    





    
    


    