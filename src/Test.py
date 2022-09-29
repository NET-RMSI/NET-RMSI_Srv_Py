import TCPServer, LoggerModule
import threading


if __name__ == '__main__':
    task0 = threading.Thread(target=LoggerModule.LOGGINGINIT)
    task0.start()
    task0.join()
    
    TCPServer.TCPSRVMAIN()



        




    
    


    
   
    
        
    


    
   
