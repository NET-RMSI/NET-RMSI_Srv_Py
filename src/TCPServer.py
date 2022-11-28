#!/usr/bin/python3
import socket
import threading
from _global import *
from EventLogging import *
from ClientHandling import *

clientlist = []

class TCPServer:
   def __init__(self, ipaddress, port):
      
      self.ipaddress = ipaddress
      self.port = port
      
      self.srvaddress = (self.ipaddress, self.port)
      self.tcpserver = None
      #self.clientlist[]
      
   def TCPServerMain(self):
      
      self.tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
         self.tcpserver.bind(self.srvaddress)
      
      except Exception as ex:
         LOGEVENTS_ERROR(f"{ex}")
         LOGEVENTS_CRITICAL(f"Terminating NET-RMSI_Srv_Py")
         self.tcpserver.close()
         quit(code=1)
   
      
      self.tcpserver.listen(4)
      
      LOGEVENTS_DEBUG(f"TCPServer listening on {PORT}")
      LOGEVENTS_DEBUG('Waiting for client to connect')
      
      # Calling tcpserver.send() throws an exeception when there is no connection, possible replacement of while loop with try and except?
      
      while True:
         
         tcpcli, (cliaddress, cliport) = self.tcpserver.accept()
         LOGEVENTS_DEBUG(f"Connected to {cliaddress}")
         
         self.tcpserver.settimeout(10.0)
         indata = self.tcpserver.recv(4096).decode('utf-8')
       
         if indata == f"{controllercli}":
            self.tcpserver.send("valid".encode())
            LOGEVENTS_INFO(f"Recieved: {indata}")
            LOGEVENTS_INFO(f"{controllercli} at {self.ipaddress} identified")
            clitype = controllercli
            

         elif indata == f"{controlledcli}":
            self.tcpserver.send("valid".encode())
            LOGEVENTS_INFO(f"Recieved: {indata}")
            LOGEVENTS_INFO(f"{controlledcli} at {self.ipaddress} identified")
            clitype = controlledcli
            
      
         else:
            self.tcpserver.send("invalid".encode())
            LOGEVENTS_INFO(f"Recieved: {indata}")
            LOGEVENTS_CRITICAL("Failed to recieve client identifier, unknown client")
            LOGEVENTS_CRITICAL(f"Closing connection to {self.ipaddress}")
            self.tcpserver.close()
         
         tcpclient = ClientHandling(cliaddress, cliport, tcpcli, clitype).start()
         
         # Append the above with addition of client type for easier referencing.
         
         clientlist.append(tcpclient)
   
   
   
 
         
'''

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
      
    
'''
      
      
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
