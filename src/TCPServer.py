#!/usr/bin/python3
from dataclasses import dataclass
import socket






def TCPSRVINIT():

   global tcpconstatus
   tcpconstatus = False

   HOSTNAME = socket.gethostname()
   PORT = 13062
   IPADDRESS = socket.gethostbyname(HOSTNAME)
   global tcpsrv
   tcpsrv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   tcpsrv.bind((IPADDRESS, PORT))

   tcpsrv.listen(1)
   print(f"Waiting for a client to connect")
   global tcpcli, address
   tcpcli, address = tcpsrv.accept()
   with tcpcli:
      print(f"Connected by {address}")
      tcpconstatus = True
      
def TCPDATACOLLECTION():
   while (tcpconstatus == True):
      with tcpcli:
         global data
         data = tcpcli.recvfrom(4096)
   
         