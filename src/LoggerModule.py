from distutils.debug import DEBUG
import datetime
import logging


def LOGGINGINIT():

    
    logging.basicConfig (filename= 'NET-RMSI_Srv_Py.log', encoding='utf-8', level=logging.DEBUG)
    
    LOGEVENTS_INFO(f"Logging started")

def LOGEVENTS_INFO(input):

    currentdateandtime = datetime.datetime.now()
    currentdateandtimestr = currentdateandtime.strftime("%m/%d/%Y, %H:%M:%S")
    
    logging.info(f"{currentdateandtimestr} " + input)

def LOGEVENTS_DEBUG(input):

    currentdateandtime = datetime.datetime.now()
    currentdateandtimestr = currentdateandtime.strftime("%m/%d/%Y, %H:%M:%S")
    
    logging.debug(f"{currentdateandtimestr} " + input)

def LOGEVENTS_ERROR(input):

    currentdateandtime = datetime.datetime.now()
    currentdateandtimestr = currentdateandtime.strftime("%m/%d/%Y, %H:%M:%S")
    
    logging.error(f"{currentdateandtimestr} " + input)

def LOGEVENTS_CRITICAL(input):

    currentdateandtime = datetime.datetime.now()
    currentdateandtimestr = currentdateandtime.strftime("%m/%d/%Y, %H:%M:%S")
    
    logging.critical(f"{currentdateandtimestr} " + input)




