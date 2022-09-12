import socket
# Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg="Hello UDP server"
# sendto()
client_socket.sendto(msg.encode('utf-8'),('127.0.0.1', 12345))
#recvfrom()
data,adrr = client_socket.recvfrom(4096)
print("Server says")
print(str(data))
# close
client_socket.close()