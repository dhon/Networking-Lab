# TCP_Client

from socket import *
serverPort = 12000
ip = '127.0.0.1'

again = "Y"

while (again=="y") | (again=="Y"):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((ip, serverPort))

    message = raw_input("\ninput Operation Code and two Integers: ")
    print ("\n ")
    print ("-->> At Client message to send out: '" + message + "'")
    
    clientSocket.send(message.encode())
    
    modifiedMessage = clientSocket.recv(1024)
    
    print ("<<-- At Client message received: '" + \
           modifiedMessage.decode() + "'")
    again = raw_input("Do you want to repeat? (y or n)")

clientSocket.close()