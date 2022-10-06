#!/usr/bin/python3
import socket
import threading
from _global import *
from LoggerModule import *
from DataProcessing import *

global tcpsrv, tcpcli, cliaddress

def TCPSRVMAIN():

   LOGEVENTS_DEBUG("Starting TCPServer")
   
   tcpsrv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      tcpsrv.bind((IPADDRESS, PORT))
      LOGEVENTS_DEBUG("Bound to socket")
   except Exception as ex:
      LOGEVENTS_ERROR(f"{ex}")
      LOGEVENTS_CRITICAL(f"Terminating NET-RMSI_Srv_Py")
      quit(code=1)

   tcpsrv.listen(2)
   LOGEVENTS_DEBUG(f"TCPServer listening on {PORT}")

   LOGEVENTS_DEBUG('Waiting for client to connect')
   
   while True:
      SRVACCEPTCON(tcpsrv)

def SRVACCEPTCON(tcpsrv):
   tcpcli, cliaddress = tcpsrv.accept()
   LOGEVENTS_DEBUG(f"Connected to {cliaddress}")
   threading.Thread(target=CLIENTIDENTIF(tcpcli, cliaddress)).start()
      
    