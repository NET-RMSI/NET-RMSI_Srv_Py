import threading
from LoggerModule import *

class TCPClient(threading.Thread):
   def __init__(self, ipaddress, port, connection):
      threading.Thread.__init__(self)
      
      self.ipaddress = ipaddress
      self.port = port
      
      self.connection = connection
      
      self.clientidentif()
      
   def clientidentif(self):
       while True:
           
        self.connection.settimeout(10.0)
        indata = self.connection.recv(4096).decode('utf-8')
       
        if indata == f"{controllercli}":
            self.connection.send("valid".encode())
            LOGEVENTS_INFO(f"Recieved: {indata}")
            LOGEVENTS_INFO(f"{controllercli} at {self.ipaddress} identified")
            #CTRLHANDLING(cliconn)

        elif indata == f"{controlledcli}":
            self.connection.send("valid".encode())
            LOGEVENTS_INFO(f"Recieved: {indata}")
            LOGEVENTS_INFO(f"{controlledcli} at {self.ipaddress} identified")
            #CTRLDHANDLING(cliconn, cliaddress)
      
        else:
            self.connection.send("invalid".encode())
            LOGEVENTS_INFO(f"Recieved: {indata}")
            LOGEVENTS_CRITICAL("Failed to recieve client identifier, unknown client")
            LOGEVENTS_CRITICAL(f"Closing connection to {self.ipaddress}")
            #cliconn.close()
            
       
       
       
       


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

    
       
        
    