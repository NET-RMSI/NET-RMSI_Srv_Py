
from concurrent.futures import process
from logging import Logger
from multiprocessing import pool
import TCPServer, LoggerModule
import multiprocessing


if __name__ == '__main__':
    multiprocessing.Process(target= LoggerModule.LOGGINGINIT)
    if LoggerModule.LOGGINGINIT() == True:
        multiprocessing.Process(target= TCPServer.TCPSRVINIT(13061))
        
        multiprocessing.Process(target= TCPServer.TCPSRVINIT(13062))
        multiprocessing.Process.start()
        

        
    



# Figuring out structure for multiprocessing
#if __name__ == '__main__':
#    multiprocessing.set_start_method('spawn')
#    with multiprocessing.Pool(processes= 4) as pool:
#        pool.apply_async(LoggerModule.LOGGINGINIT())
#        if LoggerModule.LOGGINGINIT() == True:
#            pool.apply_async(TCPServer.TCPSRVINIT(13061))
#            pool.apply_async(TCPServer.TCPSRVINIT(13062))
        



    
   
    
        
    


    
   
