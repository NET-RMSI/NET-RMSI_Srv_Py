import sqlite3
import os

def DB_Init():
        if os.path.isfile(""):
            os.remove("")
        
        con = sqlite3.connect("conclistat.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE client(alias, ipaddress, status)")
        
class DBHandler:
    def __init__(self, alias, ipaddress, status):
        
        self.alias = alias
        self.ipaddress = ipaddress
        self.status = status
    
    
    def DB_Write(self):
        pass
    
    def DB_Read(self):
        pass

