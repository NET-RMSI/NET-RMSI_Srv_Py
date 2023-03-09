import threading
from modules.req.EventLogging import *
from _global import *
from socket import socket 

clientlist = {}
clientlist_lock = threading.Lock()

class ClientHandling(threading.Thread):
    def __init__(self, cliaddress, cliport, tcpcli, clitype):
        threading.Thread.__init__(self)
        
        self.ipaddress = cliaddress
        self.port = cliport
      
        self.connection = tcpcli
        self.type = clitype
        
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
                    try:
                        rawdata = self.connection.recv(4096).decode()
                 
                        [cmdipaddr, execcmd] = str.split(rawdata, sep='/')
                    
                    except Exception as ex:
                        LOGEVENTS_ERROR(ex)
                        LOGEVENTS_INFO("Recieved data does not contain a '/' separating the IP address from the execution command")
                        
                    if int(execcmd) == 0|1:
                    # Possibly another solution would be for this code to be called from the server.
                        with clientlist_lock:
                            if clientlist[cmdipaddr] == cmdipaddr:
                                LOGEVENTS_DEBUG(f"Specified IP address found in dictonary keys: {cmdipaddr}")
                                
                                for clientlist[cmdipaddr] in clientlist:
                                    clientlist[cmdipaddr].send(int(execcmd))
                                    
                            else:
                                LOGEVENTS_ERROR(f"Specified IP address not found in dictonary keys: {cmdipaddr}")
                                
                    else:
                        LOGEVENTS_ERROR(f"Invalid execution command recieved: {execcmd}")
                      
                    self.connection.close()
                    
                    #else:
                    #    LOGEVENTS_ERROR(f"Invalid data syntax recieved: {rawdata}")
                    #    LOGEVENTS_INFO("In some cases this results from an error but this exception may be due to the client sending empty packets upon connection")
                        
            elif self.type == controlledcli:
                with clientlist_lock:
                    clientlist[self.ipaddress] = self.connection
                    
        
                LOGEVENTS_INFO("Controlled client thread, waiting for commands from a controller thread")
                    