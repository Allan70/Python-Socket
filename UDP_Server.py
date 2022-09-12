import socket

# socket()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind()
sock.bind(('127.0.0.1', 12345))

while True:
    # recv.from()
    data,addr = sock.recvfrom(4096)
    print(str(data))

    message = bytes("Hello I am UDP server".encode('utf-8'))
    # sendto()
    sock.sendto(message,addr)