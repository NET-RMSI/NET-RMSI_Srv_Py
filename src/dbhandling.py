import pymongo
from _global import *
from LoggerModule import *

def DBHANDLINGINIT():
    dbclient = pymongo.MongoClient(f'mongodb://{DBIPADDRESS}:{DBPORT}/')
    

    dbcheck = dbclient.list_database_names()
    if DBNAME in dbcheck:
        LOGEVENTS_INFO(f"{DBNAME} Exists on mongodb server")
    else:
        serverdb = dbclient[f"{DBNAME}"]

        



