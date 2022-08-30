#!/usr/bin/python3
import socket



def TCPSRV():

   PORT = 13062
   IPADDRESS = socket.gethostname()
   tcpsrv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   tcpsrv.bind((IPADDRESS, PORT))

   tcpsrv.listen(1)
   print(f"Waiting for a client to connect")
   tcpcli, address = tcpsrv.accept()
   with tcpcli:
      print(f"Connected by {address}")
      while True:
         data = tcpcli.recv(1024)
         if not data:
            break
         tcpcli.sendall(data)

      
   
