#!/usr/bin/python3
import socket
import threading
from _global import *
from LoggerModule import *
from ThreadHandling import *

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
         
         client = (cliaddress, cliport, tcpcli)
         self.clients.append(client)
         
         #LOGEVENTS_DEBUG(f"Connected to {cliaddress}")
         #threading.Thread(target=CLIENTIDENTIF(tcpcli, cliaddress)).start()
         # Add client class for threading above please!
         
      
         
         

         
         
      
      
   
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


def CLIENTIDENTIF(cliconn, cliaddress):
   
   # Check if client version is compatable with the server version
   cliconn.settimeout(10.0)
   cliid = cliconn.recv(4096).decode('utf-8')
   
   if cliid == f"{controllercli}":
      cliconn.send("valid".encode())
      LOGEVENTS_INFO(f"Recieved: {cliid}")
      LOGEVENTS_INFO(f"{controllercli} at {cliaddress} identified")
      CTRLHANDLING(cliconn)

   elif cliid == f"{controlledcli}":
      cliconn.send("valid".encode())
      LOGEVENTS_INFO(f"Recieved: {cliid}")
      LOGEVENTS_INFO(f"{controlledcli} at {cliaddress} identified")
      CTRLDHANDLING(cliconn, cliaddress)
      
   else:
      cliconn.send("invalid".encode())
      LOGEVENTS_INFO(f"Recieved: {cliid}")
      LOGEVENTS_CRITICAL("Failed to recieve client identifier, unknown client")
      LOGEVENTS_CRITICAL(f"Closing connection to {cliaddress}")
      cliconn.close()
      return
      
    