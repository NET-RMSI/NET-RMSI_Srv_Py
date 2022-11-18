import threading
import queue
from LoggerModule import *
import random

tcpqueue = queue.Queue()

# Controller client handling handoff to tcp threads assigned a controlled client.
def CTRLHANDLING(associp, execcmd):
    while True:
        # Insert code here to allow webserver/bot to control through tcp.
        tcpqueue.put(associp, execcmd)


# Controlled client handling incoming commands from other threads and carrying out exec.
def CTRLDHANDLING(connaddress):
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
        
        elif associp == connaddress:
            LOGEVENTS_INFO(f"Matching client IP and command recieved: IP: {associp} Command: {execcmd} ")
            # Insert control code/function call here please
            tcpqueue.task_done()
        
        else:
            LOGEVENTS_INFO(f"IP mismatch for client attached to thread, recieved: IP: {associp} ")
            tcpqueue.put(associp, execcmd)
            tcpqueue.task_done()