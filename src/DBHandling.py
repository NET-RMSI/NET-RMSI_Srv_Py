import pymongo
from _global import *
from LoggerModule import *


def DBHANDLER(address, status):
    dbclient = pymongo.MongoClient(f'mongodb://{DBIPADDRESS}:{DBPORT}/')
    

    dbcheck = dbclient.list_database_names()
    
    if DBNAME in dbcheck:
        LOGEVENTS_INFO(f"{DBNAME} Exists on mongodb server")


        dbclient.close()

    else:
        LOGEVENTS_INFO(f"{DBNAME} Created on mongodb server")
        serverdb = dbclient[f"{DBNAME}"]

        servercol = serverdb[f"{COLNAME}"]
        LOGEVENTS_INFO(f"{COLNAME} Created on mongodb server")
        
        dbclient.close()



    
    




        



