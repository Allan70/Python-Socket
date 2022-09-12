import socket

from _thread import *
serversocket = socket.socket()

host="127.0.0.1"
port=1233
ThreadCount = 0

try:
    # Bind()
    serversocket.bind((host, port))
except socket.err as e:
    print(str(e))

print("Waiting four connections")
serversocket.listen(5)

def client_thread(connection):
    connection.send("Welcome to the server")
    while True:
        data = connection.recv(2048)
        reply = "Write I am server" + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()
    
while True:
    client, address = serversocket.accept()
    print("Connected to"+address[0]+str(address()))
    start_new_thread(client_thread,(client,))
    ThreadCount+=1
    print("Thread number %s" %str(ThreadCount))
serversocket.close()
