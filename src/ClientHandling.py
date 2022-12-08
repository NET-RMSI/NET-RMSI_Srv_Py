import threading
import queue
from EventLogging import *
#from TCPServer import clientlist
import socket
from _global import *

class ClientHandling(threading.Thread):
    def __init__(self, ipaddress, port, connection, type):
        threading.Thread.__init__(self)
        self.ipaddress = ipaddress
        self.port = port
      
        self.connection = connection
        
        self.type = type
        
    def run(self):
        # Temporary untested fix! May need changed
        from TCPServer import clientlist
        
        if self.type == controllercli:
            while True:
                rawdata = self.connection.recv(4096).decode()
                if "/" in rawdata:
                    with str.split(rawdata, sep='/') as dataextractlist:
                        cmdipaddr = dataextractlist[0]
                        execcmd = dataextractlist[1] 
                        
                    if execcmd == 0|1:
                    # Possibly another solution would be for this code to be called from the server.
                        for tcpclient in clientlist: 
                
                            if tcpclient.clitype == controlledcli & tcpclient.cliaddress == cmdipaddr:  
                                tcpclient.connection.send(self.execcmd)
                    
                else:
                    LOGEVENTS_ERROR(f"Invalid data syntax recieved: {rawdata}")
                    LOGEVENTS_INFO("In some cases this results from an error but this exception may be due to the client sending empty packets upon connection")
                        
        elif self.type == controlledcli:
            LOGEVENTS_INFO("Controlled client thread, waiting for commands from a controller thread")
                    

        

'''
tcpqueue = queue.Queue()

# Controller client handling handoff to tcp threads assigned a controlled client.
# cliconn - Tcp server instance.
# associp - ip address of intended command recipient. 
def CTRLHANDLING(cliconn):
    while True:
        # Insert code here to allow webserver/bot to control through tcp.
        
        execcmd = cliconn.recv()
        
        tcpqueue.put(associp, execcmd)


# Controlled client handling incoming commands from other threads and carrying out exec.
# cliconn - Tcp server instance.
# connaddress - tcp ip address of connected client
def CTRLDHANDLING(cliconn, connaddress):
    while True:
        threading.Lock.acquire()
        try:
            associp, execcmd = tcpqueue.get()
       
        except Exception as ex:
            LOGEVENTS_INFO(f"{ex}")
            LOGEVENTS_INFO(f"Retrying in between 5 and 10 seconds ")
            # Test usage of random float values to stagger the threads from grabbing the same queue item over and over.
            threading.Event.wait(random.uniform(5, 10))   
        
        finally:
            threading.Lock.release()

        if execcmd != 0 | 1 :
            LOGEVENTS_ERROR(f"Invalid execution command sent to client thread: {execcmd}")
            tcpqueue.task_done()
        
        elif associp == connaddress:
            LOGEVENTS_INFO(f"Matching client IP and command recieved: IP: {associp} Command: {execcmd} ")
            # Insert control code/function call here please
            tcpqueue.task_done()
        
        else:
            LOGEVENTS_INFO(f"IP mismatch for client attached to thread, recieved: IP: {associp} ")
            tcpqueue.put(associp, execcmd)
            tcpqueue.task_done()
            
'''