#!/usr/bin/python
import socket
import random

# -------------- Global Variables --------------
Estado = 'Sumando1'

# -------------- Port Set Up --------------
host = socket.gethostname()
port = 1234
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#mySocket.bind(('localhost', 1234))  # Socket LoopBack
mySocket.bind((host, port))  # Socket LoopBack Host
#mySocket.bind(('192.168.1.132', 1234))  # Socket wlan0 inet addr:192.168.1.132
mySocket.listen(2) # 5 TPC Cons cap

# -------------- Main --------------
try:
    while True:
        (recvSocket, address) = mySocket.accept()
        Rx = recvSocket.recv(1024);
        print Rx
        Rx = Rx.split()[1][1:]
        print "trozo: "+Rx
        if Estado == 'Sumando1':    # -------- Estado 1 --------

            Sumando1 = int(Rx)
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
            "<html><body><h1>Sumador:</h1>" +
            "<hr>" +
            "<p>Primer sumando: " + str(Sumando1) + "</p>" +
            "</body></html>\r\n")
            recvSocket.send("<html><body><h4>Introduzca segundo sumando</h4>"+
            "</body></html>\r\n")

            Estado = 'Sumando2'
        elif Estado == 'Sumando2':  # -------- Estado 2 --------

            Sumando2 = int(Rx)
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
            "<html><body><h1>Sumador:</h1>" +
            "<hr>" +
            "<p>Primer sumando: " + str(Sumando1) + "</p>" +
            "<p>Segundo sumando: " + str(Sumando2) + "</p>" +
            "</body></html>\r\n")
            recvSocket.send("<em><b><big><i><b><strong><ins>"+str(Sumando1)+" + "+str(Sumando2)+
            " = "+
            str((Sumando1+Sumando2)) + "</em></b></big></i></b></strong></ins>" +
            "</body></html>\r\n")

            Estado = 'Sumando1'
        else:
            Estado = 'Sumando1'
            
        recvSocket.close()
except KeyboardInterrupt:
    mySocket.close()
    print("\nExiting Ok")



 
