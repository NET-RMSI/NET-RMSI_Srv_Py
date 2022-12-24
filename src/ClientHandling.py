import threading
from EventLogging import *
from _global import *

clientlist = set()
clientlist_lock = threading.Lock()

class ClientHandling(threading.Thread):
    def __init__(self, ipaddress, port, connection, type):
        threading.Thread.__init__(self)
        
        self.ipaddress = ipaddress
        self.port = port
      
        self.connection = connection
        self.type = type
        
    def run(self):
        
        with clientlist_lock:
            clientlist.add(self.connection)
        
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
                            
                            for self.connection in clientlist:
                
                                if self.type == controlledcli & self.ipaddress == cmdipaddr:  
                                    self.connection.send(int(execcmd))
                                    break
            
                                else:
                                    LOGEVENTS_ERROR("Requested client IP Address either does not exist in clientlist or the type of client is a controller type.")
                                    break
                                
                    else:
                        LOGEVENTS_ERROR(f"Invalid execution command recieved: {execcmd}")
                        break
            
                with clientlist_lock:
                    
                    clientlist.remove(self.connection)
                    self.connection.close()
                    
                    #else:
                    #    LOGEVENTS_ERROR(f"Invalid data syntax recieved: {rawdata}")
                    #    LOGEVENTS_INFO("In some cases this results from an error but this exception may be due to the client sending empty packets upon connection")
                        
            elif self.type == controlledcli:
                LOGEVENTS_INFO("Controlled client thread, waiting for commands from a controller thread")
                    