# TCP_Server

from socket import *
serverPort = 12000
ip = '127.0.0.1'

while True:
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((ip,serverPort))
    serverSocket.listen(1)
    print ('The TCP server is ready to receive')
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    print ("-->> At Server receved message is: '" + message + "'")

    # Tokenize the input
    a = message.split()
    # Try to convert relevant strings to integer
    try:
        b = int(a[1])
        c = int(a[2])
    # If error, set a empty so it activates next error checker
    except ValueError:
        a = []
    # Check input length, and make sure has proper OC
    if(len(a) != 3 or a[0] not in ('+', '-', '*', '/')):
        modifiedMessage = "status code 300: -1"
    # Check which OC code and do the relevant math function
    else:
        if(a[0] == '+'):
            modifiedMessage = "status code 200: " + str(b + c)
        elif(a[0] == '-'):
            modifiedMessage = "status code 200: " + str(b - c)
        elif(a[0] == '*'):
            modifiedMessage = "status code 200: " + str(b * c)
        elif(a[0] == '/'):
            if(c != 0):
                modifiedMessage = "status code 200: " + str(b / c)
            else:
                # Cannot divide by 0
                modifiedMessage = "status code 300: -1"

    print ("<<-- At Server modified message to send back: '" + modifiedMessage + "'\n")
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()