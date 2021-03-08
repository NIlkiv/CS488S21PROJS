import socket
import time

# Create server
ServerName = 'localhost'
ServerPort = 1200
ServerAddress = (ServerName, ServerPort)

# Create client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP socket

# Ask for connection to server
clientSocket.connect(ServerAddress)

# three-way handshake is performed
# a TCP connection is established between the client and server.
start = time.time()
Byt = 0
while 1:
   # start = time.time()
    # Create message
    message = input("Enter the lower case message: ")
   # byte = bytes(message, 'utf-8')
    # Send message
    clientSocket.send(message.encode('utf-8'))

    # Receive from server
    modified_sent = clientSocket.recvfrom(2048)

    # Print received message
   # print("From server:", len(modified_sent))
    Byt = Byt + len(modified_sent)
    end = time.time()
    elp = end - start
    if elp >= 5:
        break
   # else:
   # continue
print(str("BYTES: " + str(Byt) + "/" + str(elp) + "time"))
bandwith = int(Byt)/int(elp)
print("Bandwith = " + str(bandwith))
# Close connection
clientSocket.close()
