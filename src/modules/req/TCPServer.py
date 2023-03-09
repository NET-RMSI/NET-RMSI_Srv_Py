#!/usr/bin/python3
import socket
import threading
from _global import *
from modules.req.EventLogging import EventLogger as EL
from modules.req.ClientHandling import ClientHandling

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
         EL(f"{ex}").LOGEVENTS_ERROR()
         EL(f"Terminating NET-RMSI_Srv_Py").LOGEVENTS_CRITICAL()
         self.tcpserver.close()
         quit(code=1)
      
      self.tcpserver.listen(4)
      
      EL(f"TCPServer listening on {PORT}").LOGEVENTS_DEBUG()
      EL('Waiting for client to connect').LOGEVENTS_DEBUG()
      
      # Calling tcpserver.send() throws an exeception when there is no connection, possible replacement of while loop with try and except?
      
      while True:
         
         tcpcli, (cliaddress, cliport) = self.tcpserver.accept()
         EL(f"Connected to {cliaddress}").LOGEVENTS_DEBUG()
         
         indata = tcpcli.recv(4096).decode('utf-8')
       
         if indata == f"{controllercli}":
            tcpcli.send("valid".encode())
            EL(f"Recieved: {indata}").LOGEVENTS_INFO()
            EL(f"{controllercli} at {cliaddress} identified").LOGEVENTS_INFO()
            clitype = controllercli

         elif indata == f"{controlledcli}":
            tcpcli.send("valid".encode())
            EL(f"Recieved: {indata}").LOGEVENTS_INFO()
            EL(f"{controlledcli} at {cliaddress} identified").LOGEVENTS_INFO()
            clitype = controlledcli
      
         else:
            tcpcli.send("invalid".encode())
            EL(f"Recieved: {indata}").LOGEVENTS_INFO()
            EL("Failed to recieve client identifier, unknown client").LOGEVENTS_CRITICAL()
            EL(f"Closing connection to {cliaddress}").LOGEVENTS_CRITICAL()
            tcpcli.close()
            
            continue
         
         ClientHandling(cliaddress, cliport, tcpcli, clitype).start()
         
      
                    
      
         
   
   
   
