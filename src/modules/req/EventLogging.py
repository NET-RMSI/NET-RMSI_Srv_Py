import datetime
import logging
from _global import *

class EventLogger():
    def __init__(self, input):
        self.input = input
    
    def LoggingInit(self):
        
        logging.basicConfig (filename= 'NET-RMSI_Srv_Py.log', encoding='utf-8')
    
        EventLogger(f"Logging started").LOGEVENTS_INFO()
        EventLogger(f"Server Version: {serverversion}").LOGEVENTS_INFO()
    
    def LOGEVENTS_INFO(self):

        currentdateandtimestr = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    
        print(f"{currentdateandtimestr} " + self.input)
        logging.info(f"{currentdateandtimestr} " + self.input)

    def LOGEVENTS_DEBUG(self):

        currentdateandtimestr = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        print(f"{currentdateandtimestr} " + self.input)
        logging.debug(f"{currentdateandtimestr} " + self.input)

    def LOGEVENTS_ERROR(self):

        currentdateandtimestr = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        print(f"{currentdateandtimestr} " + self.input)
        logging.error(f"{currentdateandtimestr} " + self.input)

    def LOGEVENTS_CRITICAL(self):
    
        currentdateandtimestr = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        print(f"{currentdateandtimestr} " + self.input)
        logging.critical(f"{currentdateandtimestr} " + self.input)





