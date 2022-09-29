from http import server
import socket

from LoggerModule import LOGEVENTS_CRITICAL, LOGEVENTS_ERROR, LOGEVENTS_INFO



def DATAPROCESSING(cliconn):
   
   global serverversion,controlledcli,controllercli

   serverversion = "SV001"
   controllercli = "CR001"
   controlledcli = "CD001"

   while True:
      cliconn.send(f"{serverversion}")
      cliid = cliconn.recvmsg(4096)

      if cliid == f"{serverversion}":
         LOGEVENTS_ERROR(f"{serverversion} Identified")
         LOGEVENTS_CRITICAL("Another Server attempted to connect to the server")
         LOGEVENTS_CRITICAL("Closing Connection")
         cliconn.close()
         LOGEVENTS_CRITICAL("Terminating NET-RMSI_Srv_Py")
         quit()
      elif cliid == f"{controllercli}":
         LOGEVENTS_INFO(f"{controllercli} Identified")
      elif cliid == f"{controlledcli}":
         LOGEVENTS_INFO(f"{controlledcli} Identified")

   



      




    