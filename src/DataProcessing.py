import socket
from _global import *
from LoggerModule import LOGEVENTS_CRITICAL, LOGEVENTS_ERROR, LOGEVENTS_INFO

def DATAPROCESSING(cliconn, connaddress):
   
   
   with cliconn:
      socket.socket.send(f"{serverversion.encode()}")
      cliid = socket.socket.recvmsg(4096)
   
   if cliid == f"{controllercli}":
      LOGEVENTS_INFO(f"{controllercli} at {connaddress} identified")
   elif cliid == f"{controlledcli}":
      LOGEVENTS_INFO(f"{controlledcli} at {connaddress} identified")
   else:
      LOGEVENTS_CRITICAL("Failed to recieve client identifier, unknown client")
      LOGEVENTS_CRITICAL(f"Closing connection to {connaddress}")
      cliconn.close()
      return
         

         

   



      




    