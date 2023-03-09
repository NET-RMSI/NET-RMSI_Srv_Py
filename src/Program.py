#!/usr/bin/python3
import threading
from modules.req.EventLogging import *
from modules.req.TCPServer import *
from _global import *
from modules.req.FlaskWebApp import webapp
from modules.req.DBHandling import *


    
if (__name__ == '__main__'):
    
    threading.Thread(target=webapp.run(host="127.0.0.1", port=13065, debug=True)).start()
    
        
    #Start logging.
    LoggingInit()
    
    try:
        from modules.opt.LCDController import *
        LCDINIT()
        threading.Thread(target=LCDROUTINE).start()
    except Exception as ex:
        LOGEVENTS_ERROR(f"{ex}")
        LOGEVENTS_INFO("Ignore above errors if LCD module has not been installed due to lack of an LCD screen on/or connected to the hardware")
    
    TCPServer(IPADDRESS, PORT).TCPServerMain()

else:
    LOGEVENTS_ERROR("Attempted code execution from an indirect source")
    LOGEVENTS_CRITICAL(f"Terminating NET-RMSI_Srv_Py")
    quit(code=1)
    

    
    





    
    


    