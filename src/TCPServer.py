from multiprocessing.connection import wait
import socket


PORT = 13062
tcpsrv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsrv.bind((socket.gethostname(), PORT))
tcpsrv.listen(1)
tcpcli, address = tcpsrv.accept()


while True:
   print ("Connected")
   wait(1000)
    
