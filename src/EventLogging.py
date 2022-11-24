import datetime
import logging
from _global import *


def LoggingInit():

    
    logging.basicConfig (filename= 'NET-RMSI_Srv_Py.log', encoding='utf-8')
    
    LOGEVENTS_INFO(f"Logging started")
    LOGEVENTS_INFO(f"Server Version: {serverversion}")
    

def LOGEVENTS_INFO(input):

    currentdateandtimestr = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    
    print(f"{currentdateandtimestr} " + input)
    logging.info(f"{currentdateandtimestr} " + input)

def LOGEVENTS_DEBUG(input):

    currentdateandtimestr = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print(f"{currentdateandtimestr} " + input)
    logging.debug(f"{currentdateandtimestr} " + input)

def LOGEVENTS_ERROR(input):

    currentdateandtimestr = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print(f"{currentdateandtimestr} " + input)
    logging.error(f"{currentdateandtimestr} " + input)

def LOGEVENTS_CRITICAL(input):
    
    currentdateandtimestr = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print(f"{currentdateandtimestr} " + input)
    logging.critical(f"{currentdateandtimestr} " + input)




