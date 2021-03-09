import socket
import time
# Create server
serverPort = 1200
ServerName = 'localhost'
ServerAddress = (ServerName, serverPort)

# Create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associate server port number with the socket
serverSocket.bind(ServerAddress)

# wait for some client to knock on the door
serverSocket.listen(1) # maximum number of queued connections (atleast 1)

print('The server is ready to listen')
# Create connection socket
connection_socket, addr = serverSocket.accept()
start = time.time()
while  True:
    # Receive message from client
    message = connection_socket.recv(2048)
    
    # Modify the message
    modified_message = message
    
    while True:
    # Send the modified message
        connection_socket.send(modified_message)
        print("Reply sent", addr)
# Close communication with client
        end = time.time()
        elp = end - start
        if elp >= 1:
            break
    if elp >= 10:
        break
connection_socket.close()
