#_global.py contains and assigns global variables that multiple modules/scripts need access to, while preventing conflicts.
import socket


serverversion = "SV001"
controllercli = "CR001"
controlledcli = "CD001"


HOSTNAME = socket.gethostname()
PORT = 13062

#IPADDRESS = socket.gethostbyname(HOSTNAME)
#Comment out the above if running the server on a unix based system, testing indicates that parsing the IP address leads to listening on localhost.
#IPADRESS = '' Listens on all ports, if a specific adress is needed replace the field with so.
IPADDRESS = '' 