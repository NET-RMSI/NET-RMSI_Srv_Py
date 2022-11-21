#!/usr/bin/python3
import socket
import threading
from _global import *
from LoggerModule import *
from ThreadHandling import *
from TCPClient import * 

global tcpsrv, tcpcli, cliaddress
            
class TCPServer:
   def __init__(self, ipaddress, port):
      
      self.ipaddress = ipaddress
      self.port = port
      
      self.srvaddress = (self.ipaddress, self.port)
      self.tcpserver = None
      self.clients = []
   
   def socket_open(self):
      
      self.tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
         self.tcpserver.bind(self.srvaddress)
      
      except Exception as ex:
         LOGEVENTS_ERROR(f"{ex}")
         LOGEVENTS_CRITICAL(f"Terminating NET-RMSI_Srv_Py")
         self.tcpserver.close()
         quit(code=1)
   
   def accept_connections(self):
      
      self.socket_open()
      self.tcpserver.listen(4)
      
      LOGEVENTS_DEBUG(f"TCPServer listening on {PORT}")
      LOGEVENTS_DEBUG('Waiting for client to connect')
      
      while True:
         tcpcli, (cliaddress, cliport) = self.tcpserver.accept()
         LOGEVENTS_DEBUG(f"Connected to {cliaddress}")
         
         tcpclient = TCPClient(cliaddress, cliport, tcpcli).start()
         
         self.clients.append(tcpclient)
         
         self.tcpserver.close()
         
       
         
      
         
         

         
         
      
'''      
   
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

   tcpsrv.listen(4)
   LOGEVENTS_DEBUG(f"TCPServer listening on {PORT}")

   LOGEVENTS_DEBUG('Waiting for client to connect')
   
   while True:
      SRVACCEPTCON(tcpsrv)
      

def SRVACCEPTCON(tcpsrv):
   tcpcli, cliaddress = tcpsrv.accept()
   LOGEVENTS_DEBUG(f"Connected to {cliaddress}")
   threading.Thread(target=CLIENTIDENTIF(tcpcli, cliaddress)).start()

'''
