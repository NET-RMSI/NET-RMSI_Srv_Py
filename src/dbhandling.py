import pymongo
from _global import *

def DBHANDLINGINIT():
    dbclient = pymongo.MongoClient(f'mongodb://{DBIPADDRESS}:{DBPORT}/')
    serverdb = dbclient["srv_pconndb"]



