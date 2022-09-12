import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind the socket
server_socket.bind(("localhost", 12345))
server_socket.listen(5) #Keep waiting if the server is busy for 5 secs

while True:
    print("Server waiting for connection")
    client_socket,addr=server_socket.accept()
    print("client connected from", addr)
    while True:
        data=client_socket.recv(1024)
        if not data or data.decode('utf-8') == 'END':
            break;
        print("received from client client :%s" %data.decode('utf-8'))
        try:
            client_socket.send(bytes('May client', 'utf-8'))
        except:
            print("Exited by user")
    client_socket.close()