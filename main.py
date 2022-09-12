# The code below uses TCP to connect to a remote server. 
# To connect to 'python.org' enter www.python.org in the target host 
# Enter '80' in the target port
# This will make a connection via TCP and port 80 to the website
# www.python.org
import socket
import sys

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("Failed to create a socket.")
    print("Reason"+str(err))
    sys.exit()
print("Socket create")

target_host = input("Enter the target host name to connect :")
target_port = input("Enter the target port :")

try:
    sock.connect((target_host, int(target_port)))
    print("Socket Connected to %s on port: %s" %(target_host,target_port))
    sock.shutdown(2)
except socket.error as err:
    print ("Failed to connect to %s on port %s" %(target_host, target_port))
    print("Reason %s" %str(err))
    sys.exit()
