#!/usr/bin/python3
from logging import Logger
import socket
from LoggerModule import LOGEVENTS_CRITICAL, LOGEVENTS_DEBUG, LOGEVENTS_ERROR


def TCPSRVINIT(PORT):

   LOGEVENTS_DEBUG(f'Starting TCPServer')

   HOSTNAME = socket.gethostname()
   #PORT = 13062
   IPADDRESS = socket.gethostbyname(HOSTNAME)
   

   global tcpsrv
   tcpsrv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      tcpsrv.bind((IPADDRESS, PORT))
      LOGEVENTS_DEBUG(f'Bound to socket')
   except Exception as ex:
      LOGEVENTS_ERROR(f"{ex}")
      LOGEVENTS_CRITICAL(f"Terminating NET-RMSI_Srv_Py")
      quit()
   
   tcpsrv.listen(2)
   LOGEVENTS_DEBUG(f'TCPServer listening on {PORT}')
   
   print(f"Waiting for a client to connect")

   LOGEVENTS_DEBUG(f'Waiting for client to connect')
   global tcpcli, address
   tcpcli, address = tcpsrv.accept()
   with tcpcli:
      print(f"Connected by {address}")
      
      LOGEVENTS_DEBUG(f'Connected by {address}')

      return True
      
def TCPDATACOLLECTION():
   while True:
      with tcpcli:
         data = tcpcli.recv(4096)
         if not data:
            break


         
         

   
         