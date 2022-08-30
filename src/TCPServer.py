#!/usr/bin/env python3
from http import client
from multiprocessing.connection import Client
import socket




PORT = 13062
tcpsrv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsrv.bind((socket.gethostname(), PORT))

tcpsrv.listen(1)
   
tcpcli, address = tcpsrv.accept()
with tcpcli:
   print(f"Connected by {address}")
   while True:
      data = tcpcli.recv(1024)
      if not data:
         break
      tcpcli.sendall(data)

      
   
