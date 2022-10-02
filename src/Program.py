#!/usr/bin/python3
import threading
from LoggerModule import *
from LCDController import *
from TCPServer import *
from _global import *


if (lcdmoduleenabled == True and __name__ == '__main__'):
    LCDINIT()
    LOGGINGINIT()
    task0 = threading.Thread(target=LOGGINGINIT)
    task0.start()
    task0.join()

    threading.Thread(target=LCDROUTINE).start()

    TCPSRVMAIN()

    
elif(__name__ == '__main__'):
    LOGGINGINIT()
    TCPSRVMAIN()

else:
    LOGEVENTS_ERROR("Attempted code execution from an indirect source")
    LOGEVENTS_CRITICAL(f"Terminating NET-RMSI_Srv_Py")
    quit()
    





    
    


    