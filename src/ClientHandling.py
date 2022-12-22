import threading
import queue
from EventLogging import *
import socket
from _global import *
import TCPServer


class ClientHandling(threading.Thread):
    def __init__(self, ipaddress, port, connection, type):
        threading.Thread.__init__(self)
        self.ipaddress = ipaddress
        self.port = port
      
        self.connection = connection
        
        self.type = type
        
    def run(self):
        
        if self.type == controllercli:
            
            while True:
                '''
                # Debugging block
                try:
                    rawdata = self.connection.recv(4096).decode()
                    LOGEVENTS_DEBUG(rawdata)
                except Exception as ex:
                    LOGEVENTS_ERROR(ex)
                '''
                rawdata = self.connection.recv(4096).decode()
                #if "/" in rawdata:
                [cmdipaddr, execcmd] = str.split(rawdata, sep='/')
                        
                if int(execcmd) == 0|1:
                        # Possibly another solution would be for this code to be called from the server.
                        TCPServer.TCPServer.MessageClients(ipaddr=cmdipaddr, cmd=execcmd)
                else:
                    LOGEVENTS_ERROR(f"Invalid execution command recieved: {execcmd}")
                    
                #else:
                #    LOGEVENTS_ERROR(f"Invalid data syntax recieved: {rawdata}")
                #    LOGEVENTS_INFO("In some cases this results from an error but this exception may be due to the client sending empty packets upon connection")
                
                        
        elif self.type == controlledcli:
            LOGEVENTS_INFO("Controlled client thread, waiting for commands from a controller thread")
                    