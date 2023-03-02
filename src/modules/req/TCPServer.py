#!/usr/bin/python3
import socket
import threading
from _global import *
from EventLogging import *
from ClientHandling import ClientHandling

class TCPServer:
   def __init__(self, ipaddress, port):
      
      self.ipaddress = ipaddress
      self.port = port
      
      self.srvaddress = (self.ipaddress, self.port)
      self.tcpserver = None
      
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
         
         indata = tcpcli.recv(4096).decode('utf-8')
       
         if indata == f"{controllercli}":
            tcpcli.send("valid".encode())
            LOGEVENTS_INFO(f"Recieved: {indata}")
            LOGEVENTS_INFO(f"{controllercli} at {cliaddress} identified")
            clitype = controllercli

         elif indata == f"{controlledcli}":
            tcpcli.send("valid".encode())
            LOGEVENTS_INFO(f"Recieved: {indata}")
            LOGEVENTS_INFO(f"{controlledcli} at {cliaddress} identified")
            clitype = controlledcli
      
         else:
            tcpcli.send("invalid".encode())
            LOGEVENTS_INFO(f"Recieved: {indata}")
            LOGEVENTS_CRITICAL("Failed to recieve client identifier, unknown client")
            LOGEVENTS_CRITICAL(f"Closing connection to {cliaddress}")
            tcpcli.close()
            
            continue
         
         ClientHandling(cliaddress, cliport, tcpcli, clitype).start()
         
      
                    
      
         
   
   
   
