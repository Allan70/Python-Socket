import socket

# Create our socket object. 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client_socket.connect(('127.0.0.1', 12345))
payload="Hello there Sir. Allan"

try:
    while True:
        # Send data to the server
        client_socket.send(payload.encode('utf-8'))
        # receive data from the server
        data = client_socket.recv(1024)
        print(str(data))
        more = input("Want to send score data to the server")
        if more.lower() == 'y':
            payload = input("Enter payload")
        else:
            break
except KeyboardInterrupt:
        print("Excited by the user")
client_socket.close()
        

    # Receive data from the server