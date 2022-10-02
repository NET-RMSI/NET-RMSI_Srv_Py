import socket
#Change this value dependant if server hardware has a compatible LCD screen
lcdmoduleenabled = False

serverversion = "SV001"
controllercli = "CR001"
controlledcli = "CD001"

HOSTNAME = socket.gethostname()
PORT = 13062
IPADDRESS = socket.gethostbyname(HOSTNAME)