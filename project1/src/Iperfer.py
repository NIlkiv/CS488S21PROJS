import socket
import time
import sys
import pickle

# Create server
ServerName = sys.args()    #input("Enter Hostname ")
if ServerName == 0 or ServerName == '':
    print("Error: missing or additional arguments")
    sys.exit()

ServerIP = socket.gethostbyname(ServerName)
ServerPort = sys.args()    #input("Enter Port from range 1024 - 65535: ") #takes in port
if ServerPort == '':
    print("Error: missing or additional arguments")
    sys.exit()

if int(ServerPort) < 1024 or int(ServerPort) > 65535:
    print(f"Port {ServerPort} out of range")
    sys.exit()

sendTime = sys.args()      #input("Enter time in seconds ")
if sendTime == '':
    print("Error: missing or additional arguments")
    sys.exit()

if int(sendTime) < 0:
    print("Error: missing or additional arguments")
    sys.exit()

# Create client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP socket

# Ask for connection to server
clientSocket.connect((ServerName, int(ServerPort)))

# three-way handshake is performed
# a TCP connection is established between the client and server.

start = time.time()                 #takes computer local time
Byt = [0] * 1000                    #Array of 1000 elements set to all 0s
data_string = pickle.dumps(Byt)     #Array to Byte data conversion
byt = 0                             #initial byte sent count

while 1:
    clientSocket.send(data_string) #sends packets

    modified_sent = clientSocket.recvfrom(2048)  #receive return from server
       
    byt = byt + len(modified_sent)   #start count of bytes sent by the length of Byt array
    end = time.time()                #get 2nd local time form machine to establish end time
    elp = end - start                #total time elapsed

    if elp >= float(sendTime):       #if the elapsed time is greater than time usr entered end the count and break the loop
        break

   # else:
   # continue
#print(str("BYTES: " + str(byt) + "/" + str(elp) + "time")) #print total bytes sent + time elapsed

bandwith = (int(byt)/int(elp))/1024                                              #calc bandwith
print("Sent=" + str(byt) + " kB " + "rate="  + str(bandwith) + "Mbps")           #print bandwith
                                                           
clientSocket.close()                                                             #close port
