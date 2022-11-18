#_global.py contains and assigns global variables that multiple modules/scripts need access to, while preventing conflicts.

#Server, Controlled and controller client versioning numbers. Do not change as this will break things.
serverversion = "SV100"
controllercli = "CR100"
controlledcli = "CD100"


# IP address and port of the server.
IPADDRESS = ''
PORT = 13062

# IP address and port to allow connection to a MongoDB database.
DBIPADDRESS = ''
DBPORT = ''
# MongoDB database and collection names.
DBNAME = "srv_pconndb"
COLNAME = "connections"
 