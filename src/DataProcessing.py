from _global import *
from LoggerModule import LOGEVENTS_CRITICAL, LOGEVENTS_ERROR, LOGEVENTS_INFO

def CLIENTIDENTIF(cliconn, connaddress):
   
   # Check if client version is compatable with the server version
   cliid = cliconn.recvmsg(4096)
   
   if cliid == f"{controllercli}":
      cliconn.send("valid".encode())
      LOGEVENTS_INFO(f"{controllercli} at {connaddress} identified")
   elif cliid == f"{controlledcli}":
      cliconn.send("valid".encode())
      LOGEVENTS_INFO(f"{controlledcli} at {connaddress} identified")

      
   else:
      cliconn.send("invalid".encode())
      LOGEVENTS_CRITICAL("Failed to recieve client identifier, unknown client")
      LOGEVENTS_CRITICAL(f"Closing connection to {connaddress}")
      cliconn.close()
      return
         

         

   



      




    