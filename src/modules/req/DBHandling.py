import sqlite3
import os


class DBHandler:
    def __init__(self, alias, ipaddress, status):
        
        self.alias = alias
        self.ipaddress = ipaddress
        self.status = status
        self.con = sqlite3.connect("conclistat.db")
        self.cursor = self.con.cursor()

    def DB_Init(self):
        if os.path.isfile(""):
            os.remove("")
            
        self.cursor.execute("CREATE TABLE client(alias, ipaddress, status)")
        
    def DB_Write(self):
        pass
    
    def DB_Read(self):
        pass

